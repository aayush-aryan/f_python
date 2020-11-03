"""
author -Aayush Aryan
date -03-11-2020
time -14:45
package -Basicpython

Statement-Write a Python program to determine if variable is defined or not.

"""
def variableDefineOrNot():
 try:
   name = "aayush"
 except NameError:
   print("Variable is not defined....!")
 else:
   print("Variable is defined.")
 try:
  age
 except :
   print("Variable is not defined....!")
 else:
  print("Variable is defined.")
  
  variableDefineOrNot()