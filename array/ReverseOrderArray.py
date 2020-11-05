"""
author -Aayush Aryan
date -04-11-2020
time -16:40
package -array

Statement-Write a Python program to reverse the order of the items in the array.

"""
class ReverseOrderArray:
    def reverse(self,arrOfNum):
        '''
         @:parameter:self
         @:parameter:arrOfNum
        '''
        print("Original array: " + str(arrOfNum))
        arrOfNum.reverse()
        print("Reverse array: " + str(arrOfNum))
arr = ReverseOrderArray()
rangeVal = int(input("Enter the size of the array : "))
arrOfNum = []
for index in range(rangeVal):
    val = int(input("Enter the element of array : "))
    arrOfNum.append(val)
arr.reverse(arrOfNum)