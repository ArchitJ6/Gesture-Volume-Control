import cv2
import time
import math
import numpy as np
import HandTrackingHelper
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Constants:
wCam, hCam = 1280, 720
volume_bar = 400
volume_per = 0

# Set the previous time
pTime = 0

# Create the HandTrackingHelper object
detector = HandTrackingHelper.handDetector(detectionConfidence = 0.7)

# Get the volume controller
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Get the volume range
volume_range = volume.GetVolumeRange()
min_volume = volume_range[0]
max_volume = volume_range[1]

# Set the camera
cap = cv2.VideoCapture(0)

# Set the width and height of the camera
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    # Find the hands
    img = detector.findHands(img)
    # Find the position of the hands
    landmark_list = detector.findPosition(img, draw = False)

    if len(landmark_list) != 0:
        # Get the positions of the Thumb_Tip
        x1, y1 = landmark_list[4][1], landmark_list[4][2]
        # Get the positions of the Index_Finger_Tip
        x2, y2 = landmark_list[8][1], landmark_list[8][2]

        # Get the center of the line
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        # Draw a line between the Thumb_Tip and the Index_Finger_Tip
        cv2.circle(img, (x1, y1), 15, (255, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 255, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)
        cv2.circle(img, (cx, cy), 15, (255, 255, 0), cv2.FILLED)

        # Get the length of the line
        length = math.hypot(x2 - x1, y2 - y1)

        # Hand range: 50 - 550
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        elif length > 550:
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
        else:
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

        # Convert the length to volume range
        volume_level = np.interp(length, [50, 550], [min_volume, max_volume])
        volume_bar = np.interp(length, [50, 550], [400, 150])
        volume_per = np.interp(length, [50, 550], [0, 100])
        volume.SetMasterVolumeLevel(volume_level, None)
    
    # Display the volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volume_bar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volume_per)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Display the FPS
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display the image
    cv2.imshow("Video", img)

    # Graceful exit with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()