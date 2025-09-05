# pip install psutil
# CTRL + J Terminal 

import psutil
import time
import time

battery = psutil.sensors_battery()


def battery_Alert():
    print("Battery Alert Function Started")
    plugged_in = psutil.sensors_battery().power_plugged
    fully_charged_notified = False
    low_battery_notified = False

    while True:
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        is_plugged = battery.power_plugged

        # Check if fully charged and unplugged
        if percentage == 100 and not is_plugged:
            if not fully_charged_notified:
                print("100% charged. Please unplug it.")
                fully_charged_notified = True
        else:
            fully_charged_notified = False  # Reset notification when unplugged or charging

        # Check for low battery when unplugged
        if not is_plugged:
            if percentage <= 20 and not low_battery_notified:
                if percentage <= 5:
                    print("Sir, Sorry to disturb you but this is your last chance, charge your system now")
                elif percentage <= 10:
                    print("Sir, Sorry to disturb you but we are running on very low battery power")
                elif percentage <= 20:
                    print("Sir, Sorry to disturb you but battery is low now")
                low_battery_notified = True
            elif percentage > 20:
                low_battery_notified = False  # Reset when battery goes above 20%
        else:
            low_battery_notified = False  # Reset if plugged in

        time.sleep(10)


def check_plug1():
    print("Checking Charging Status...")
    previous_state = None  # Initialize previous state as None

    while True:
        battery = psutil.sensors_battery()
        current_state = battery.power_plugged

        # Check if the state has changed
        if current_state != previous_state:
            if current_state:
                print("Charging status : Started")
            else:
                print("charging status : Stopped")
            
            previous_state = current_state  # Update the previous state

        time.sleep(1) 

def check_battery():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    plugged = battery.power_plugged

    # Base status message
    if plugged:
        status = f"🔋 Hey, your system is running on {percent}% and it is connected to power."
    else:
        status = f"🔋 Hey, your system is running on {percent}% and it is not connected to power."

    # Suggestion logic
    suggestion = ""
    if not plugged and percent <= 20:
        suggestion = "⚠️ Please plug in your charger soon to avoid shutdown."
    elif plugged and percent >= 95:
        suggestion = "🔌 You can unplug the charger now to save battery health."
    elif not plugged and percent > 50:
        suggestion = "✅ Battery level is good, no need to plug in right now."
    elif plugged and percent < 95:
        suggestion = "🔄 Keep charging until it reaches a healthy level."
    else:
        suggestion = "👌 Your system is fine."

    return f"{status} {suggestion}"

