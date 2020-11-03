"""
author - ${Aayush Aryan}
date - ${03-11-2020}
time - ${08:45am}
package - ${Basicpython}
Title -"Write a Python program to get the name of the host on which the routine is running."

"""
import socket
try:
 HostName = socket.gethostname()
 print()
 print("Host name:", HostName)
 print()
except:
    print("CheckedInbuiltMethod")