# <h1 align="center">Jetson Finger Mouse</h1>
Jetson Finger Mouse is a project that turns your finger into a mouse using [Jetson Inference](https://github.com/dusty-nv/jetson-inference).

## Instalation

### 1. Cloning the respository
Change directories into you `jetson-inference` folder and run the Docker container:
```bash
cd jetson-inference
./docker/run.sh
```
Clone the repository:
```bash
git clone https://github.com/TheCamBloch/JetsonFingerMouse
```

### 2. Prerequisites
Install the required packages and modules:
```bash
apt-get install python3-tk python3-dev
pip3 install pyautogui xlib
```
>**Note:** `apt-get update` might be necessary

## Running the project
The project can be run by simply executing the `main.py` file:
```bash
cd JestsonFingerMouse
python3 main.py
```

After loading the model, a window should pop up showing the webcam stream with bounding boxes. The cursor should move to the center of the bounding box.
<img src="https://lh3.googleusercontent.com/pw/AIL4fc-LWDWeD4-Q9lskQttd-U6RKPfndc9yJ5jEdtTdrtAtuSBJ5-fIBjuscIxc6L6xHbS4CPL914uYweecFvCJ1b_785LUXDdry_9pkyR1fqGJHlOL9Q=w2400" alt="Running the model" align="center"/>

## How it works
This model is a retrained version of `ssd_mobilenet_v2`. I took pictures of my hand in various positions and labeled it using the `camera-capture tool`. Then, using `train_ssd.py`, I utilized transfer learning to teach the network. As for the main python file, I used the Center attribute of the network's detections to be passed into `pyautogui.moveTo()`.