# Gesture-Volume-Control 🎵✋  

Easily control your system volume with simple hand gestures! This project leverages **OpenCV**, **MediaPipe**, and **Pycaw** to track hand movements and adjust the system volume dynamically. Say goodbye to keyboard shortcuts and volume buttons—just move your hand to set the volume!  

---

## 📌 Features  
✅ **Real-time Hand Tracking** – Uses OpenCV and MediaPipe to detect and track hand movements efficiently.  
✅ **Gesture-Based Volume Control** – Adjust system volume by changing the distance between your thumb and index finger.  
✅ **Smooth & Responsive** – Optimized for real-time performance with minimal latency.  
✅ **Cross-Platform Support** – Works on **Windows, macOS, and Linux**.  
✅ **Lightweight & Easy to Use** – Requires minimal dependencies and runs with basic system resources.  

---

## 🖥️ Supported Operating Systems  
| OS       | Supported |  
|----------|-----------|  
| Windows  | ✅ Yes  |  
| macOS    | ✅ Yes  |  
| Linux    | ✅ Yes  |  

💡 **Note:** On **Linux and macOS**, ensure Pycaw alternatives like `pactl` (PulseAudio) or `os.system` commands are used for volume control.  

---

## 🚀 Installation  

Follow these steps to set up and run the project:  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/ArchitJ6/Gesture-Volume-Control.git
cd Gesture-Volume-Control
```

### 2️⃣ Install Dependencies  
Ensure you have Python **3.7+** installed. Then, run:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application  
```bash
python VolumeHandControl.py
```

---

## 🏗️ How It Works  
The application captures video through the webcam and uses **MediaPipe** to detect hand landmarks. By measuring the distance between the **thumb and index finger**, it maps the distance to the system's volume level, adjusting it in real time.  

📌 **Hand Gestures:**  
- Move your thumb and index finger **closer** ➝ 🔈 Decrease volume  
- Move them **farther apart** ➝ 🔊 Increase volume  

---

## 🛠️ Configuration  
You can tweak the sensitivity and behavior inside `VolumeHandControl.py`. Some key parameters:  
- **Min/Max Hand Distance** – Defines the range for volume scaling.  
- **Frame Rate Optimization** – Adjust camera frame processing speed.  

---

## 📥 Cloning (For Development)  
If you want to contribute or modify the project, clone it:  
```bash
git clone https://github.com/ArchitJ6/Gesture-Volume-Control.git
cd Gesture-Volume-Control
```

---

## 🤝 Contributing  
We welcome contributions! 🚀  

### Steps to contribute:  
1️⃣ **Fork the repository** 🍴  
2️⃣ **Create a new branch** (`git checkout -b feature-branch`) 🌱  
3️⃣ **Make your changes** and commit (`git commit -m "Your message"`) 📝  
4️⃣ **Push your changes** (`git push origin feature-branch`) 📤  
5️⃣ **Submit a pull request** 🔀  

Feel free to add new features, optimize performance, or improve the UI! 🎉  

---

## 📜 License  
This project is licensed under the **MIT License**. 🆓