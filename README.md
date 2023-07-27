# Jetson Finger Mouse

Jetson Finger Mouse is a project that turns your finger into a mouse.

## Instalation

### 1. Requirements
Install the requirements using Bash:
```bash
apt-get install python3-tk python3-dev
pip3 install pyautogui python-xlib
```
>**Note** `apt-get update` might be necessary
### 2. Cloning the respository
Change directories into you `jetson-inference` folder and run the Docker container:
```bash
cd jetson-inference
./docker/run.sh
```
Clone the repository:
```bash
git clone https://github.com/TheCamBloch/JetsonFingerMouse
```
## Running the project
The project can be run by simply executing the `main.py` file:
```bash
python3 main.py
```
After loading the model, a window should pop up showing the webcam stream with bounding boxes.
[View a video explanation here](video link)
