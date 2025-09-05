


# # Task.py
# import os
# import subprocess
# import webbrowser
# import pyautogui as gui
# import subprocess
# import time

# import psutil
# import pygetwindow as gw
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # def open_app(app_name: str):
# #     """Open applications dynamically (supports classic and UWP apps)."""
# #     app_name = app_name.lower()

# #     apps = {
# #         "notepad": "notepad.exe",
# #         "chrome": "chrome.exe",
# #         "vscode": "code.exe",
# #         "cmd": "cmd.exe",
# #         "calculator": "calc.exe",        # UWP alias
# #         "settings": "ms-settings:",      # UWP protocol
# #         "camera": "microsoft.windows.camera:",  # UWP protocol
# #         "controlpanel": "control.exe",
# #         "youtube": "https://youtube.com"  # opens in browser
# #     }

# #     if app_name in apps:
# #         try:
# #             if apps[app_name].endswith(":") or apps[app_name].startswith("http"):
# #                 # Open UWP protocol or website
# #                 os.system(f'start {apps[app_name]}')
# #             else:
# #                 # Classic .exe apps
# #                 subprocess.Popen(apps[app_name])
# #             return f"✅ Opened {app_name}"
# #         except Exception as e:
# #             return f"❌ Failed to open {app_name}: {str(e)}"
# #     else:
# #         return f"❌ Unknown app: {app_name}"

# def open_app(text: str):
    
#     try:
#        subprocess.run(text)
#     except Exception as e:
#         gui.press("win")
#         time.sleep(0.2)
#         gui.write(text)
#         time.sleep(0.2)
#         gui.press("enter")

# def close_app(app_name: str):
#     closed = False

#     # 1. Try psutil kill
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             if app_name.lower() in proc.info['name'].lower():
#                 print(f"🛑 Killing {proc.info['name']} (PID: {proc.info['pid']})")
#                 proc.kill()
#                 closed = True
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             continue

#     # 2. If not closed, try taskkill (Windows native)
#     if not closed:
#         try:
#             result = subprocess.run(
#                 ["taskkill", "/f", "/im", f"{app_name}.exe"],
#                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
#             )
#             if "SUCCESS" in result.stdout:
#                 print(f"✅ {app_name} closed via taskkill")
#                 closed = True
#         except Exception:
#             pass

#     # 3. Fallback for UWP apps → find window & send Alt+F4
#     if not closed:
#         windows = gw.getWindowsWithTitle(app_name)
#         if windows:
#             print(f"⚠️ Closing UWP app window: {windows[0].title}")
#             windows[0].activate()
#             time.sleep(0.5)
#             gui.hotkey("alt", "f4")
#             closed = True

#     if not closed:
#         print(f"❌ Could not close {app_name}")

#     return closed


# def write_on(app: str, topic: str):
#     """Write content into supported apps (basic version)."""
#     app = app.lower()

#     if app == "notepad":
#         file_path = "note.txt"
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(topic)
#         subprocess.Popen(["notepad.exe", file_path])
#         return f"📝 Wrote into Notepad: {topic}"

#     elif app == "vscode":
#         file_path = "note.py"
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(topic)
#         subprocess.Popen(["code.exe", file_path])
#         return f"📝 Wrote into VS Code: {topic}"

#     else:
#         return f"❌ Writing on {app} not supported yet."


# def handle_task(intent: dict):
#     """Main dispatcher for handling tasks dynamically."""
#     intent_name = intent.get("intent")
#     slots = intent.get("slots", {})

#     if intent_name == "open_app":
#         return open_app(slots.get("app", ""))
#     elif intent_name == "close_app":
#         return close_app(slots.get("app", ""))
#     elif intent_name == "write_on":
#         return write_on(slots.get("app", "notepad"), slots.get("topic", ""))
#     else:
#         return "🤔 I don’t know how to handle this command yet."


from .AppController.AppControl import *
from .Battery.Battery import check_battery
from .Brightness.Brightness import set_brightness_level
from .FileHandeling.Create_File_Folder import create_file_on_desktop
from .FileHandeling.Create_File_Folder import create_folder
from .SetVolume.SetVolume import set_volume_windows
from .Camera.TakeCamera import take_photo
from .ScrollFunction.Scroll import *
from .Tab_Automation.Tab_automation import *
from .MessageHandeing.Message import send_message
from .RunCode.Run import run_vscode
from .WifiBluthuth.WifiBt import *

# ---------------- Intent Dispatcher ---------------- #
def handle_task(intent: dict):
    """Main dispatcher for handling tasks dynamically."""
    intent_name = intent.get("intent")
    slots = intent.get("slots", {})

    if intent_name == "open_app":
        return open_app(slots.get("app", ""))
    elif intent_name == "close_app":
        return close_app(slots.get("app", ""))
    elif intent_name == "write_on":
        return write_on(slots.get("app", "notepad"), slots.get("topic", ""))
    elif intent_name == "check_battery":
        return check_battery()
    elif intent_name == "set_brightness":
        return set_brightness_level(slots.get("topic"))
    elif intent_name == "create_file":
        return create_file_on_desktop(slots.get("topic"))
    elif intent_name == "create_folder":
        return create_folder(intent['slots'])
    elif intent_name == "set_volume":
        return set_volume_windows(slots.get("topic"))
    elif intent_name == "take_photo":
        return take_photo()
    elif intent_name == "scroll_up":
        return scroll_up()
    elif intent_name == "scroll_down":
        return scroll_down()
    elif intent_name == "scroll_to_top":
        return scroll_to_top()
    elif intent_name == "scroll_to_bottom":
        return scroll_to_bottom()
    elif intent_name == "open_new_tab":
        return open_new_tab()
    elif intent_name == "close_tab":
        return close_tab()
    elif intent_name == "open_browser_menu":
        return open_browser_menu()
    elif intent_name == "zoom_in":
        return zoom_in()
    elif intent_name == "zoom_out":
        return zoom_out()
    elif intent_name == "refresh_page":
        return refresh_page()
    elif intent_name == "switch_to_next_tab":
        return switch_to_next_tab()
    elif intent_name == "switch_to_previous_tab":
        return switch_to_previous_tab()
    elif intent_name == "open_history":
        return open_history()
    elif intent_name == "open_bookmarks":
        return open_bookmarks()
    elif intent_name == "go_back":
        return go_back()
    elif intent_name == "go_forward":
        return go_forward()
    elif intent_name == "open_dev_tools":
        return open_dev_tools()
    elif intent_name == "toggle_full_screen":
        return toggle_full_screen()
    elif intent_name == "open_private_window":
        return open_private_window()
    elif intent_name == "send_message":
        return send_message(slots.get("app"), slots.get("to"),slots.get("topic"))
    elif intent_name == "run_code":
        return run_vscode()
    elif intent_name == "on_wifi":
        return wifi_control(True)
    elif intent_name == "off_wifi":
        return wifi_control(False)
    elif intent_name == "on_bluetooth":
        return bluetooth_control(False)
    elif intent_name == "off_bluetooth":
        return bluetooth_control(False) 
    elif intent_name == "search_on":
        return search_on(slots.get("topic"),slots.get("app"))
    elif intent_name == "minimize_tab":
        return minimize_tab()
    elif intent_name == "maximize_tab":
        return maximize_tab()
    elif intent_name == "separate_tab":
        return separate_tab()   
    else:
        return "🤔 I don’t know how to handle this command yet."














