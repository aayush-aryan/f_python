"""
author - ${Aayush Aryan}
date - ${03-11-2020}
time - ${09:20am}
package - ${Basicpython}
Title -"Write a Python program to get system command output."

"""
import subprocess
try:
 returnedText = subprocess.check_output("dir", shell=True, universal_newlines=True)
 print("dir command to list file and directory")
 print(returnedText)
except:
    print("CheckInbuiltMethodAndImportLibrary")