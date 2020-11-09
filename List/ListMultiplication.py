"""
author -aayush aryan
date -07-11-2020
time -19:10
package -List
problem Statement-Write a Python program to multiplies all the items in a list.
"""
class ListMultiplication:
    def findMultiply(self,ListOfNum):
        """
               #Create a method fo list element and multiply
                @param dListOfNum: multiply the list element
                @return: output after the multiplication
               """
        sum = 1
        for x in ListOfNum:
            sum *= x
        print("Multiplication Of List Items is : ",sum)
try :
    rangeVal = int(input("Enter The no of elenent in set : "))
    ListOfNum = [ ]
    for i in range(rangeVal):
        val = int(input("Enter The  element of list : "))
        ListOfNum.append(val)
    print("List Data : ",ListOfNum)

except OverflowError:
    print("check the output")

if __name__ == '__main__':

    listData = ListMultiplication()
    listData.findMultiply(ListOfNum)