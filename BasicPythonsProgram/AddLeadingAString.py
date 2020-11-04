"""
author -Aayush Aryan
date -03-11-2020
time -15:20
package -Basicpython

Statement-Write a Python program to add leading zeroes to a string.

"""
def addedLeadingZerostoString():
 print("\nAdded leading zeros:")
 try:
  str1="aayush"
  str1 = str1.rjust(8, '0')
  print(str1)
  str1 = str1.rjust(10, '0')
  print(str1)
 except:
     print("enterValidStringValues")

addedLeadingZerostoString()