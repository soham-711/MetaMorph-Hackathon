import psutil
import subprocess
import time
import pyautogui
from ..AppController.AppControl import open_app

def take_photo():
   print("📷 Opening Camera app...")
   open_app("Camera")
   time.sleep(5)  # wait for the camera to open

    # Notify user before clicking
   print("🤖 Jarvis: Please look at the camera for the best picture...")

   time.sleep(2)  # give user time to focus

    # Simulate pressing ENTER to take photo in Camera app
   pyautogui.press("enter")

   print("✅ Photo captured successfully! Saved in system storage (Camera Roll).")
