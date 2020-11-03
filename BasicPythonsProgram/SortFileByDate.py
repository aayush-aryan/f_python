"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${07:15pm}
package - ${Basicpython}
Title -"  Write a Python program to sort files by date."
"""
import glob
import os
try:
 files = glob.glob("*.txt")
 files.sort(key=os.path.getmtime)
 print("\n".join(files))
except:
    print("EnterProperFileExtension")