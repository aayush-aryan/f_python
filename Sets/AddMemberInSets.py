"""
author -Aayush Aryan
date -05-11-2020
time -12:20
package -Sets
Statement-Write a Python program to add member(s) in a set.
"""

class AddMembers:

    def toADD(self,setValue):

        """
        @param dictOfNum: input of dicOfNum is taken
        @return: return set of element
        """
        rangeVal = int(input("Enter The Range Of Values You Want To Enter : "))
        for index in range(1, rangeVal + 1):
            valAdd = input("Enter The String Or Value : ")
            setValue.add(valAdd)
        print(setValue)
    def toUpdate(self,setValue):
        rangeVal = int(input("Enter The Range Of Values You Want To Update : "))
        for i in range(1, rangeVal + 1):
            valUpdate = input("Enter The String Or Value : ")
            setValue.update([valUpdate])
        print(setValue)

setValue = set()
setMembers = AddMembers()
setMembers.toADD(setValue)
setMembers.toUpdate(setValue)