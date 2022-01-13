import subprocess

def mac_changer(interface, new_mac):
    print("[+] The MAC will be changed to " + interface + new_mac)
    
    subprocess.call(["sudo", "ifconfig" ,interface, "down"])
    subprocess.call(["sudo", "ifconfig" ,interface, "hw", "ether",new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

interface = 'wlan0'
mac = input('MAC > ')   
mac_changer(interface, mac)
