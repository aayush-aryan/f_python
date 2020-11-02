"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${4:30}
package - ${Basicpython}

Title -"Write a Python program to check whether a file exists."

"""
import os.path
try:
 open('aayush.txt', 'w')
 print(os.path.isfile('aayush.txt'))
except :
    print("ProvideProperFile")