import wmi

def set_brightness_level(level):
    try:
        level=int(level)
        if 0 <= level <= 100:
            w = wmi.WMI(namespace='wmi')
            brightness_methods = w.WmiMonitorBrightnessMethods()[0]
            brightness_methods.WmiSetBrightness(level, 0)  # 0 is the timeout in seconds
            return f"Brightness set to {level}%"
        else:
            return "Error: Brightness level must be between 0 and 100"
    except Exception as e:
        return f"Error: {e}"