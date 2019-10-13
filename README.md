# blue_ping
### Utilises L2 Ping's to detect the presence of a bluetooth device.

will require a target list to be loaded with one MAC per line
at present this list is required to be named "target_list.txt" and placed in the 
scrip directory.

run script with python3 ping.py - you may need SUDO to enable accesss to
your bluetooth device. 

Iterates though a list of MAC addresses.
Does not requere pairing to the device
Requires the BlueZ stack to be installed. 

Requires a list of bluetooth mac addresses saved in a text file called target_list.txt to be in the same directory.
Once a device has been detected the script will continually ping the device. 

Takes about 2 seconds per device to time out.
