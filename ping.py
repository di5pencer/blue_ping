## iterates though a list of bluetooth MAC addresses.
## Pings for presence and when device is detected
## continues to ping that device until it goes out of range.
import os
import subprocess
import time
import datetime as datetime
import re

from time_parse import *
from mac_check import *

#Load list of targets from text file. 
input_list = [line.rstrip('\n') for line in open("target_list.txt")]
target_list = []
rejected_list = []

#check for a valid MAC
for target in input_list:
    if checkMAC(target) == 1:
        target_list.append(target)
    else:
        rejected_list.append(target)
        Exception

#confirm load
#print(target_list)
print('\x1b[0;37;41m' + "These MAC addresses are invalid: " +
      str(rejected_list)+ '\x1b[0m')

print('\x1b[6;30;42m' + (str(len(target_list))) +
      " Valid targets loaded. \n" + '\x1b[0m')

#define function to ping devices. 
def blue_ping(target_mac):
    inrage = False
    print("Pinging target MAC " + target_mac + ".")
    n1 = datetime.datetime.now()
    response = subprocess.Popen(["l2ping", "-c 1", "-t 0.1", "-i hci0", target_mac], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response.wait()
    return_code = response.returncode
    stdout_value = response.communicate()
    n2 = datetime.datetime.now()
    #print(return_code)
    #print (stdout_value)

    ping_time = ((n2 - n1).microseconds)
    print("Timeout microseconds: " + str(ping_time))
    print("")
    
    if return_code == 0:
        inrange = True
        #print str(response)
        print('\x1b[6;30;42m' + str(target_mac) + ": In Range!" + '\x1b[0m')
        
        while inrange == True:
            response = subprocess.Popen(["l2ping", "-c 1", "-i hci0", target_mac], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            response.wait()
            return_code = response.returncode
            stdout_value, stderr_value = response.communicate()
            print('\x1b[6;30;42m' + str(target_mac) +
                  ": In Range!" + '\x1b[0m')
            decoded = stdout_value.decode('utf-8')
            try:
                packet_success = output_parse(decoded)[0]
                print(packet_success)
                flight_time = output_parse(decoded)[1]
                print(flight_time)
            except:
                break

            #print(output_parse(decoded))
            #print(stdout_value)
            #print(str(stdout_value))

            if return_code == 1:
                inrange = False

    if return_code == 1:
        print(str(target_mac) + ': Out of range')
        inrange = False

#start ping process   
while True:
    for x in target_list:
        blue_ping(x)
