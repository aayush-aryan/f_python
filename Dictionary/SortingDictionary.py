"""
author -Aayush Aryan
date -04-11-2020
time -17:55
package -dictenory
Statement-Write a Python script to sort (ascending and descending) a dictionary by
value.
"""
import operator
class SortingDictionary:
    def sorting(self, dictOfNum):
        '''
          @param:self
           @param:dictOfNum
         '''
        try:
         print('Original dictionary : ', dictOfNum)
         sortedAsc = dict(sorted(dictOfNum.items(), key=operator.itemgetter(1)))
         print('Dictionary in ascending order by value : ', sortedAsc)
         sortedDesc = dict(sorted(dictOfNum.items(), key=operator.itemgetter(1), reverse=True))
         print('Dictionary in descending order by value : ', sortedDesc)
        except:
            print("EnterValidElementForDictionary")
dictionary = SortingDictionary()
rangeVal = int(input("Enter the size of dictionary : "))
dictOfNum = { }
for index in range(1, rangeVal + 1):
    val = int(input("Enter the dictionary elements: "))
    dictOfNum.setdefault(index, val)
dictionary.sorting(dictOfNum)