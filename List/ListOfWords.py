"""
author -aayush aryan
date -07-11-2020
time -14:55
package -List
problem Statement-Write a Python program to find the list of words that are longer than n from a given list of words.
"""

class FindListOfWord:

    def long_words(self, number, str):
        """
        @param number:
        @param str
        """

        txt = str.split(" ")
        for x in txt:
            if len(x) > number:
                word_len.append(x)
        return word_len

word_len = []
try:
    n=int(input("Enter the no words: "))
    str=input("Enter the list of words: ")
except:
    print("CHECK YOIR INPUT")
if __name__ == '__main__':

    findList=FindListOfWord()
    list_of_words=findList.long_words(n,str)
    print(list_of_words)