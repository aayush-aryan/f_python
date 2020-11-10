"""
author -aayush aryan
date -09-11-2020
time -15:10
package -Strings
problem Statement-Write a Python program to reverse a string
"""

class ReverseString:

    #This method create Reverse the string
    def toReverseString(self, strVal):
        '''
        :param:strVal: Reverse the string
        :return : return after the remove
        '''

        revStr = ''
        index = len(strVal)
        while index > 0:
            revStr += strVal[index - 1]
            index = index - 1
        return revStr


if __name__ == '__main__':

    reverse_string = ReverseString()
    strVal = input("Enter a String To Reverse : ")
    print("Reverse String : ", reverse_string.toReverseString(strVal))