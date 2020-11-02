"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${06:50pm}
package - ${Basicpython}
Title -" Write a Python program to get an absolute file path."

"""
try:
 def absoluteFilePath(path_fname):
    import os
    return os.path.abspath('path_fname')
except:
    print("ProvideCorrectPathName")

print("The absolute file path are: ", absoluteFilePath("aayush.txt"))