"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${06:50pm}
package - ${Basicpython}
Title -" Write a Python program to get file creation and modification date/times."

"""
import os.path, time
try:
 print("Last modified: %s" % time.ctime(os.path.getmtime("aayush.txt")))
 print("Created: %s" % time.ctime(os.path.getctime("aayush.txt")))
except:
    print("ProvideProperFileName")