"""
author -aayush aryan
date -08-11-2020
time -13:45
package -List
problem Statement-Write a Python program to split a list based on first character of word.
"""
from itertools import groupby
from operator import itemgetter
from List.UtilityPackage import Ulility

class SplitItem:

    def split(self,word_list):
        """
        :param word_list:
        """

        for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)

if __name__ == '__main__':
    requiredList=Ulility.createList()
    split_item=SplitItem()
    split_item.split(requiredList)