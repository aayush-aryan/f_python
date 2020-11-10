"""
author -aayush aryan
date -09-11-2020
time -13:30
package -Strings
problem Statement-Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t
"""
class ChangeCharacterOccurence:

    def changeChar(str1):
      char = str1[0]
      str1 = str1.replace(char, '$')
      str1 = char + str1[1:]

      return str1

if __name__ == '__main__':
    changeCharacterOccurence=ChangeCharacterOccurence()
    str=changeCharacterOccurence.changeChar('restart')
    print(str)