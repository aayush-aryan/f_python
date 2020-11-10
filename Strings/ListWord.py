"""
author -aayush aryan
date -09-11-2020
time -13:55
package -Strings
problem Statement-Write a Python function that takes a list of words and returns the length of the longest
one
"""

class FindLongestWord:

    def longestWordLength(self,string):

        length = 0

        # Finding longest word in sentence
        for word in string.split():
            if (len(word) > length):
                length = len(word)

        return length

if __name__ == '__main__':
    find_longest=FindLongestWord()
    str1=input("Enter the string: ")
    print(find_longest.longestWordLength(str1))