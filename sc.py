import pyautogui
import time
time.sleep(5)
# Get the current mouse position
x, y = pyautogui.position()

# Calculate the coordinates of the top-left corner of the square
left = x - 32
top = y - 32

# Take a screenshot of the square
screenshot = pyautogui.screenshot(region=(left, top, 65, 65))

# Save the screenshot to a file
screenshot.save('screenshot.png')
