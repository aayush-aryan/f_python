"""
author -Aayush Aryan
date -04-11-2020
time -17:20
package -array
Statement-Write a Python program to remove the first occurrence of a specified element from an
array.
"""
class RemoveFirstOccurence:
    def removeOccurence(self,arrOfNUm,value):
        print("Original array: " + str(arrOfNum))
        arrOfNum.remove(value)
        print("Number of occurrences of the element ",value," in array: " + str(arrOfNUm.count(value)))
        print("Updated array: " + str(arrOfNum))
arr = RemoveFirstOccurence()
rangeVal = int(input("Enter the size of array : "))
arrOfNum = []
for index in range(rangeVal):
    arrayElement = int(input("Enter the element of array : "))
    arrOfNum.append(arrayElement)
Value = int(input("Enter The Value You Want To Remove : "))
arr.removeOccurence(arrOfNum,Value)