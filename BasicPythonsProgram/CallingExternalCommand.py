"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${05:05pm}
package - ${Basicpython}

Title -" Write a python program to call an external command in Python."

"""
try:
 from subprocess import call
 call(["ls", "-l"])
except:
    print("EnterProperExternalCommand")