
"""
author -Aayush Aryan
date -05-11-2020
time -11:55
package -Sets
Statement-Write a Python program to create a set.

"""
class CreateSet:

    def create(self,dictOfNum):
        """
                        @create method for set
                        @param dictOfNum: input of dicOfNum is taken
                        @return: return set of element
                    """
        emptySet = set()
        print("Empty Set : ", emptySet)
        nonEmptySet = set(dictOfNum)
        print("Non Empty Set : ", nonEmptySet)
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = [ ]
try:
    for index in range(1, rangeVal + 1):
        val = input("Enter The value : ")
        dictOfNum.append(val)
except:
    print("Check your input")
    if __name__=="__main__":
        setData = CreateSet()
        setData.create(dictOfNum)