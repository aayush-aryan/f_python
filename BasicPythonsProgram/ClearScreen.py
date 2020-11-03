"""
author - ${Aayush Aryan}
date - ${03-11-2020}
time - ${08:35am}
package - ${Basicpython}
Title -"Write a Python program to clear the screen or terminal."
"""

import os
import time
try:
 os.system("cls")
 time.sleep(2)
except:
    print("CheckeImportLibrary")

