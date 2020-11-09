"""
author -Aayush aryan
date -07-11-2020
time -11:03
package -List
problem Statement-' Write a Python function that takes two lists and returns True if they have at
least one common member.'
"""

class CommonItemsList:
    def checkCommon(self, FirstList, SecondList):
        result=False

        for i in FirstList:
            for j in SecondList:
                if i==j:
                    result=True
                    return result




FirstList=[]
try:
    a=int(input("Enter the no of element of 1st list: "))
    for i in range(a):
        value=input("Enter the element of list")
        FirstList.append(value)

    SecondList=[]
    a=int(input("Enter the no of element od 2nd list: "))
    for i in range(a):
        value=input("Enter the element of list")
        SecondList.append(value)

    print(FirstList, SecondList)
except:
    print("CHECK YOU INPUT")


if __name__ == '__main__':
    commonMember=CommonItemsList()
    print(commonMember.checkCommon(FirstList, SecondList))