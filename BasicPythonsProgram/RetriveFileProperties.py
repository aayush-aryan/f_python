"""
author - ${Aayush Aryan}
date - ${03-11-2020}
time - ${10:30am}
package - ${Basicpython}
Title -"Write a Python program to retrieve file properties."
"""
import os.path
import time
try:
 print('File         :', __file__)
 print('Access time  :', time.ctime(os.path.getatime(__file__)))
 print('Modified time:', time.ctime(os.path.getmtime(__file__)))
 print('Change time  :', time.ctime(os.path.getctime(__file__)))
 print('Size         :', os.path.getsize(__file__))
except:
    print("CheckedInbuiltFunctionAndImportStatements")