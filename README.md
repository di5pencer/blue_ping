# blue_ping
### Utilises L2 Ping's to detect the presence of a bluetooth device.

Iterates though a list of MAC addresses sending them an L2 Ping request.
Does not require you to be paired with the device
Requires the BlueZ stack to be installed. 

To operate this will require a target list to be loaded with one MAC address per line.
At present this list is required to be named "target_list.txt" and placed in the 
same folder as the script.

Run script with python3 ping.py - you may need SUDO to enable accesss to
your bluetooth device. 

Once a device has been detected the script will continually ping the device. 

Takes about 2 seconds per device to time out.
