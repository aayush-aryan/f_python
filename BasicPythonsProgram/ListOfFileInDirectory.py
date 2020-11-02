"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${05:35pm}
package - ${Basicpython}

Title -" Write a Python program to list all files in a directory in Python."

"""


from os import listdir
from os.path import isfile, join
try:
 filesList = [file for file in listdir('D:/NewPython/Basicpython') if isfile(join('D:/NewPython/Basicpython', file))]
 print(filesList);
except :
    print("provideProperDirectoryPath")