"""
author -Aayush Aryan
date -04-11-2020
time -16:40
package -array

Statement-Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.

"""
import UserUtil
class ArrayOfInteger:
    def index(self, arrayElement, indexValue):
        '''
               @:parameter:self
               @:parameter:arrayElement
               @:parameter:indexNumber
        '''
        print(arrOfNum)
        print("access first three items individually")
        print("Required Index Element : ", arrayElement[indexValue])
        print("Last Element are : ", arrayElement[-1])
        print("First Element are:", arrayElement[0])
arrayofinteger = ArrayOfInteger()
arrOfNum = []
print("enter the size of the array :")
lengthOfArray =UserUtil.inputFunction()
print("Enter the array element :")
for index in range(lengthOfArray):
    arrayElement = UserUtil.inputFunction()
    arrOfNum.append(arrayElement)
print("Enter The Index whose Value You Want To Find : ")
indexNumber = UserUtil.inputFunction()

arrayofinteger.index(arrOfNum, indexNumber)
