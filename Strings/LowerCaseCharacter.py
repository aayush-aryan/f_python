"""
author -aayush aryan
date -09-11-2020
time -14:25
package -Strings
problem Statement-Write a Python program to lowercase first n characters in a string.
"""

class First_N_LowerCaseCharacter:
    def lowerCase(self,str1,n):

        """
        :param str1:
        :param n:
        """

        print(str1[:n].lower() + str1[n:])


if __name__ == '__main__':
    first_n_lowerCase=First_N_LowerCaseCharacter()
try:
    str=input("Enter the string in Capital letter: ")
    n=int(input("enter the number at which change to lower case: "))
    first_n_lowerCase.lowerCase(str,n)

except:
    print("EnterStringTypeInput")