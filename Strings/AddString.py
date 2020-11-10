"""
author -aayush aryan
date -09-11-2020
time -14:55
package -Strings
problem Statement-Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly''
"""

class ModifiedString:
    def addString(self, str1):
        """
        :param str1:
        :return: str1
        """
        length = len(str1)

        if length > 2:
            if str1[-3:] == 'ing':
                str1 += 'ly'
            else:
                str1 += 'ing'

        return str1

if __name__ == '__main__':
    modified_string=ModifiedString()
    str=input("Enter the string: ")
    print(modified_string.addString(str))