import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def wifi_control(turn_on=True):
    state = "enable" if turn_on else "disable"
    try:
        interfaces = subprocess.check_output('netsh interface show interface', shell=True).decode()
        wifi_name = None
        for line in interfaces.splitlines():
            if "Wireless" in line or "Wi-Fi" in line:
                wifi_name = line.split()[-1]
                break

        if wifi_name:
            subprocess.run(f'netsh interface set interface "{wifi_name}" {state}', shell=True)
            logging.info(f"✅ Wi-Fi { 'ON' if turn_on else 'OFF' }")
        else:
            logging.warning("❌ No Wi-Fi interface found")

    except Exception as e:
        logging.error(f"❌ Failed to control Wi-Fi: {e}")


def bluetooth_control(turn_on=True):
    state = "Enable" if turn_on else "Disable"
    ps_command = f'''
    $bt = Get-PnpDevice -Class Bluetooth | Where-Object {{$_.Status -eq "OK"}}
    foreach ($device in $bt) {{ 
        if ("{state}" -eq "Enable") {{ Enable-PnpDevice -InstanceId $device.InstanceId -Confirm:$false }} 
        else {{ Disable-PnpDevice -InstanceId $device.InstanceId -Confirm:$false }}
    }}
    '''
    try:
        subprocess.run(["powershell", "-Command", ps_command], shell=True)
        logging.info(f"✅ Bluetooth { 'ON' if turn_on else 'OFF' }")
    except Exception as e:
        logging.error(f"❌ Failed to control Bluetooth: {e}")
