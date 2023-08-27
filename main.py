import cv2 
import pyautogui
import numpy as np
from PIL import ImageGrab
import play


print("正在检测屏幕...")
while True:
    screen_width, screen_height = pyautogui.size()
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,0,screen_width,screen_height))), cv2.COLOR_BGR2RGB)
    white_pixels = np.count_nonzero(screenshot == [255, 255, 255])
    total_pixels = screenshot.shape[0] * screenshot.shape[1]
    white_percentage = white_pixels / total_pixels * 100
    #print(round(white_percentage))
    if round(white_percentage) >= 82:
        try:
            print("Yuzusoft 启动!")
            play.run()
            break            
        except:
            print("Yuzusoft浓度不足！")
            break