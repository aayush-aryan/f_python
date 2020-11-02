"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${06:35pm}
package - ${Basicpython}

Title -"Write a python program to access environment variables.."

"""
import os
try:
# Access all environment variables
  print('*----------------------------------*')
  print(os.environ)
  print('*----------------------------------*')
# Access a particular environment variable
  print(os.environ['C:\\'])
  print('*----------------------------------*')
  print(os.environ['C:\\'])
  print('*----------------------------------*')
except:
    print("provideProperDirectory")