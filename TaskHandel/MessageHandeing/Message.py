
import pyautogui as gui
import pygetwindow as gw
import time
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from TaskHandel.AppController.AppControl import open_app

from TaskHandel.AppController.AppControl import open_app

def send_whatsapp_desktop(contact: str , message: str):
    print(contact)
    try:
        open_app("WhatsApp")
        time.sleep(5)  # wait for WhatsApp to load
        # Step 3: Search for contact
        gui.hotkey("ctrl", "f")
        time.sleep(1)
        gui.typewrite(contact)
        time.sleep(2)
        gui.press("down")
        gui.press("enter")
        time.sleep(2)
        gui.press("tab")   # first tab = profile section
        gui.press("tab") 
        gui.press("tab")   # first tab = profile section
        gui.press("tab") 
        gui.press("tab")   # first tab = profile section
        gui.press("tab") 
        gui.press("tab")   # first tab = profile section
        gui.press("tab") 
        gui.press("tab")   # first tab = profile section
        gui.press("tab") 
        time.sleep(1)
        # Step 4: Type and send message
        gui.typewrite(message)
        time.sleep(2)
        gui.press("enter")
        time.sleep(4)
        # Step 5: Close WhatsApp
        windows = gw.getWindowsWithTitle("WhatsApp")
        if windows:
            windows[0].close()
        print(f"✅ WhatsApp message sent to {contact}")
        return "success"
    except Exception as e:
        print(f"❌ WhatsApp error: {e}")
        return "failed"



def send_message(platform: str, recipient: str, message: str, **kwargs):
    """
    Unified messaging function
    :param platform: "whatsapp" | "telegram" | "facebook"
    :param recipient: contact_name (whatsapp), chat_id (telegram), username/id (fb)
    :param message: str
    :param kwargs: for extra params (e.g. bot_token for telegram)
    """
    platform = platform.lower()

    if platform == "whatsapp":
        return send_whatsapp_desktop(recipient, message)

    elif platform == "telegram":
         # Placeholder – would need Graph API or fbchat
        print("⚠️ Telegram messaging not implemented yet")
        return "failed"

    elif platform == "facebook":
        # Placeholder – would need Graph API or fbchat
        print("⚠️ Facebook messaging not implemented yet")
        return "failed"

    else:
        print("❌ Unsupported platform")
        return "failed"


# ----------------- Example Usage ----------------- #
if __name__ == "__main__":
    # WhatsApp Example
    send_message("whatsapp", "Sunal", "Tumi manko vath khaba")

    # Telegram Example
    # send_message("telegram", "123456789", "Hello from Jarvis!", bot_token="YOUR_BOT_TOKEN")
    pass