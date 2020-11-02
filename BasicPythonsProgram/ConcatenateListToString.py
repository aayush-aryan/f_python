"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${4:30}
package - ${Basicpython}

Title -" Write a Python program to concatenate all elements in a list into a string and return it."

"""
try:
 def concatenateListElement(list):
     result = ''
     for element in list:
         result += str(element)
     return result

 print(concatenateListElement(["aayush", "aryan", 2, 1994]))
except:
    print("EnterValidListElement")
