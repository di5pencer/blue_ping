
## iterates though a list of bluetooth MAC addresses.
## Pings for presence and when device is detected
## Continues to ping that device until it goes out of range.
import os
import subprocess
import time
import datetime as datetime

#Load list of targets from text file. 
target_list = [line.rstrip('\n') for line in open("target_list.txt")]

#confirm load
print(target_list)
print((str(len(target_list))) + " Targets loaded.")
print("\n")

#define function to ping devices. 
def blue_ping(target_mac):
    inrage = False
    print("Pinging target MAC " + target_mac + ".")
    n1 = datetime.datetime.now()
    response = subprocess.call(["l2ping", "-c 1", "-t 0.1", "-i hci0", target_mac])
    n2 = datetime.datetime.now()
    ping_time = ((n2 - n1).microseconds)
    print("Microseconds: " + str(ping_time))
    print("")
    
    if response == 0:
        inrange = True
        print str(response)
        print str(target_mac), "In Range!"
        
        while inrange == True:
            response = subprocess.call(["l2ping", "-c 1", "-i hci0", target_mac])
            #print str(response)
            print str(target_mac), "In Range"
            if response == 1:
                inrange = False

    if response == 1:
        print str(target_mac), 'Out of range'
        #print str(response)
        inrange = False

#start ping process   
while True:
    for x in target_list:
        blue_ping(x)
