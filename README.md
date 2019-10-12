# blue_ping
### Utilises L2 Ping's to detect the presence of a bluetooth device.

Iterates though a list of MAC addresses.
Requires the BlueZ stack to be installed. 

Requires a list of bluetooth mac addresses saved in a text file called target_list.txt to be in the same directory.
Once a device has been detected the script will continually ping the device. 

Takes about 2 seconds per device to time out.
