"""
author -Aayush Aryan
date -03-11-2020
time -16:20
package -Basicpython

Statement-Write a Python program to find files and skip directories of a given directory.

"""

import os
def findFiles():
    try:
      print([files for files in os.listdir('/Basicpython/aayush.txt') if os.path.isfile(os.path.join('/Basicpython/aayush.txt', files))])
    except:
        print("checkProperDirectory")
findFiles()
