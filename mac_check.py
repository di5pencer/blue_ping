#confirm input list contains valid MAC addresses.
import re

def checkMAC(input_mac):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", input_mac.lower()):
        return 1
    else:
        return 0

