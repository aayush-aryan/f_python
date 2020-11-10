"""
author -aayush aryan
date -09-11-2020
time -14:30
package -Strings
problem Statement-Write a Python program to calculate the length of a string.
"""

class CalulateLengthOfString:

    def stringLength(self, str1):
        """
        :param str1:
        :return: count
        """
        count = 0
        for char in str1:
            count += 1
        return count


if __name__ == '__main__':
    calulate_length=CalulateLengthOfString()
    str=input("Enter the string : ")
    print(calulate_length.stringLength(str))