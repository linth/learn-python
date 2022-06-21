import pyautogui
import time


# 目前滑鼠坐標
mourse_loc = pyautogui.position()
print(mourse_loc)

# 目前螢幕解析度
image_resolution = pyautogui.size()
print(image_resolution)

# (x,y)是否在螢幕上
x, y = 122, 244
is_screen = pyautogui.onScreen(x, y)
print(is_screen)


# while True:
#     mourse_loc = pyautogui.position()
#     print(mourse_loc)
#     time.sleep(1)