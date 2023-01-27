import pyautogui
import time
import datetime

start_time = datetime.datetime.now()
time.sleep(4)
while True:
        pyautogui.mouseDown(button='left',duration=0.1)
        pyautogui.moveRel(-65, 0, duration=0.1)
        pyautogui.mouseUp(duration=0.1)
        pyautogui.mouseDown(button='left',duration=0.1)
        pyautogui.moveTo(1771, 550, duration=0.1)
        pyautogui.mouseUp(duration=0.1)
        # dejar el mouse en el dep
        pyautogui.moveTo(931, 542, duration=0.1)
        pyautogui.mouseUp(duration=0.1)
        current_time = datetime.datetime.now()
        time_diff = current_time - start_time
        if time_diff.seconds > 720: # 12 minutes
          start_time = current_time
          pyautogui.press('f1')