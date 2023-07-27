import jetson.inference
import jetson.utils
import pyautogui

net = jetson.inference.detectNet(argv=["--model=ssd-mobilenet.onnx", "--labels=labels.txt", "--input-blob=input_0", "--output-cvg=scores", "--output-bbox=boxes"], threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0")
ScreenSize = pyautogui.size()


while display.IsStreaming():
        img = camera.Capture()
        ScaledUp = jetson.utils.cudaAllocMapped(width=ScreenSize[0], height=ScreenSize[1], format=img.format)
        jetson.utils.cudaResize(img, ScaledUp)
        detections = net.Detect(ScaledUp)
        display.Render(ScaledUp)
        jetson.utils.cudaDeviceSynchronize()
        display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        for detection in detections:
                if net.GetClassDesc(detection.ClassID) == "index":
                        pyautogui.moveTo(detection.Center)