"""
author -Aayush Aryan
date -05-11-2020
time -12:30
package -Sets
Statement-Write a Python program to create an intersection of sets.
"""
class CreateIntersection:

    def intersection(self,firstSetValue,SecondSetValue):
        '''
        @create method to intersection
        @param:firstSetvalue pass the first value
        @param:SecondSetValue pass the second value
        @return : return the insection value
                     '''
        intersectionSet = firstSetValue & SecondSetValue
        print(intersectionSet)
try:
    firstSetValue = set()
    rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
    for index in range(1, rangeVal + 1):
        valAddFirst = input("Enter The String Or Value : ")
        firstSetValue.add(valAddFirst)

        SecondSetValue = set()
        rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
    for ind in range(1, rangeVal + 1):
        valAddSecond = input("Enter The String Or Value : ")
        SecondSetValue.add(valAddSecond)
        print("Data Set First: ",firstSetValue)
        print("Data Set Second: ",SecondSetValue)
except firstSetValue:
    if __name__=="__main__":
        setMembers = CreateIntersection()
        setMembers.intersection(firstSetValue,SecondSetValue)