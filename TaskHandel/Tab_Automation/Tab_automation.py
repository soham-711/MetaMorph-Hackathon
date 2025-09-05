import pyautogui
import time

def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def open_browser_menu():
    pyautogui.hotkey('alt', 'f')

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'b')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    pyautogui.hotkey('f11')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')


def minimize_tab():
    """Minimize current window."""
    pyautogui.hotkey("win", "d")
    time.sleep(0.2)
    print("Window minimized.")

def maximize_tab():
    """Maximize or restore current window."""
    pyautogui.hotkey("win", "d")
    time.sleep(0.2)
    print("Window maximized.")

def separate_tab():
    """
    Split current app window to left or right half of the screen.
    side = 'left' or 'right'
    """
    
    pyautogui.hotkey("win", "left")
    print("Window snapped to the left.")
    time.sleep(
        2)
    pyautogui.hotkey('enter')
    print("Window snapped to the right.")
    
