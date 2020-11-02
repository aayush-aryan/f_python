"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${3:30}
package - ${Basicpython}

Title -" Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"

"""
try:
 def containedValue(listValues, number):
    for value in listValues:
        if number == value:
            return True
    return False
 print(containedValue([1, 5, 8, 3], 3))
 print(containedValue([5, 8, 3], -1))
except:
    print("plzPutValidListEntry")