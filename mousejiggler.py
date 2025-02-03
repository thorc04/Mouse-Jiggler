import pyautogui
import threading
import time
import random
from pynput import keyboard

pyautogui.FAILSAFE = False

move_mouse = False

def wiggle_mouse():
    while move_mouse:
        x, y = pyautogui.position()
        if x <= 0 or y <= 0 or x >= pyautogui.size()[0] - 1 or y >= pyautogui.size()[1] - 1:
            print("Mouse is in a corner! Moving mouse to the center.")
            center_mouse()
        else:
            x += random.randint(-100, 100)
            y += random.randint(-100, 100)
            pyautogui.moveTo(x, y, duration=1)
        time.sleep(3)

def center_mouse():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)

def on_press(key):
    global move_mouse
    try:
        if key == keyboard.Key.f5:
            move_mouse = not move_mouse
            if move_mouse:
                print("Mouse jiggler started. Press F5 to stop.")
                threading.Thread(target=wiggle_mouse).start()
            else:
                print("Mouse jiggler stopped. Press F5 to start.")
        elif key == keyboard.Key.f9:
            center_mouse()
            print("Mouse centered. Press F5 to start/stop the mouse jiggler.")
        elif key == keyboard.Key.f10:
            print("Exiting program.")
            return False
    except AttributeError:
        pass

print("Press F5 to start/stop the mouse jiggler.")
print("Press F9 to center the mouse.")
print("Press F10 to exit the program.")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()