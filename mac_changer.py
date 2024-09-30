import subprocess
import optparse
import re

print("Mac changer started")

def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest = "interface", help = "Interface to change!")
    parse_object.add_option("-m","--mac",dest = "mac_address",help = "new mac address")
    (user_input,arguments) = parse_object.parse_args()
    return user_input

def mac_changer(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

user_interface = get_input().interface
user_mac_address = get_input().mac_address
mac_changer(user_interface,user_mac_address)
finalized_mac_address = control_new_mac(str(user_interface))

if finalized_mac_address == user_mac_address:
    print("Success")
else:
    print("Error")


