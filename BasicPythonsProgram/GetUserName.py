"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${06:50pm}
package - ${Basicpython}

Title -" Write a Python program to get the current username"

"""
import getpass
try:
 print(getpass.getuser())
except:
    print("useCorrectInbuiltMethod")