"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${11:35}
package - ${Basicpython}

Title -" 2. Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"

"""
try:
 values = input("enter the number seprated by comma : ")
 list = values.split(",")
 tuple = tuple(list)
 print('Generated List are  : ',list)
 print('Generated Tuple are : ',tuple)
except:
    print("enterValidNumberSeparetedByComma")