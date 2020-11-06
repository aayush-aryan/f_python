"""
author -Aayush Aryan
date -05-11-2020
time -15:20
package -Sets
Statement-Write a Python program to iteration over sets.
"""

class IterateSets:
    def toIterate(self, setOfNum):
        """
        @create a method to iterate  the dict
         @param setOfNum: use for iterate set value
         @return: Remove the repeating value
        """
        numItrSet = set(setOfNum)
        for number in numItrSet:
            print(number)

rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = []
try:
    for index in range(1, rangeVal + 1):
        val = input("Enter The value : ")
        dictOfNum.append(val)
except ValueError:
    print("enter the correct value")
    if "__name__"=="__main__":
            setData = IterateSets()
            setData.toIterate(dictOfNum)
