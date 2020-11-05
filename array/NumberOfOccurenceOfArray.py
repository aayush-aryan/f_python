"""
author -Aayush Aryan
date -04-11-2020
time -16:40
package -array
Statement-Write a Python program to get the number of occurrences of a specified element in an
array.
"""
class NumberOfOccurenceOfArray:
    def countOccurence(self, arrOfNum, value):
        '''
            @param:self
            @param:arrOfNUm
            @param:value

            '''
        print("Original array: " + str(arrOfNum))
        print("Number of occurrences of the number ", value, " in array: " + str(arrOfNum.count(value)))
arr = NumberOfOccurenceOfArray()
rangeVal = int(input("Enter the size of the array : "))
arrOfNum = []
for index in range(rangeVal):
    arrayElement = int(input("Enterthe element of array : "))
    arrOfNum.append(arrayElement)
Value = int(input("Enter The Value You Want To Find Ocuurence of : "))
arr.countOccurence(arrOfNum, Value)