import pyautogui

x = 0
while x <= 500:
     pyautogui.click(x=375, y=1402, clicks=1000, interval=0.0000001, button='left')
     x += 1