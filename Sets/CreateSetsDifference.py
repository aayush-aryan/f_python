"""
author -Aayush Aryan
date -05-11-2020
time -12:30
package -Sets
Statement-Write a Python program to create set difference..
"""
class SetDifference:

    def difference(self,firstSetValue,SecondSetValue):
        '''
               @create method and find difference
               @param:firstSetvalue pass the first value
               @param:SecondSetValue pass the second value
               @return : return the insection value
        '''
        diffSet = firstSetValue - SecondSetValue
        print("Difference in Set : ",diffSet)
try :
    firstSetValue = set()
    rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
    for i in range(1, rangeVal + 1):
        valAddFirst = input("Enter The String Or Value : ")
        firstSetValue.add(valAddFirst)
        SecondSetValue = set()
        rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
    for i in range(1, rangeVal + 1):
        valAddSecond = input("Enter The String Or Value : ")
        SecondSetValue.add(valAddSecond)
        print("Data Set First: ",firstSetValue)
        print("Data Set Second: ",SecondSetValue)
except :
    print("errorINValue")
    if __name__=="__main__":
        setMembers = SetDifference()
        setMembers.difference(firstSetValue,SecondSetValue)