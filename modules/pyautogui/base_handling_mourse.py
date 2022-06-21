import pyautogui
import time


#用3秒時間移動滑鼠到位置 (x, y)
seconds = 3
pyautogui.moveTo(1000, 1000, duration=seconds)


pyautogui.rightClick(x=100, y=100)
pyautogui.moveTo(110, 110, duration=1)
# pyautogui.middleClick(x=moveToX, y=moveToY)
# pyautogui.doubleClick(x=moveToX, y=moveToY)
# pyautogui.tripleClick(x=moveToX, y=moveToY)
