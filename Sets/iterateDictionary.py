"""
author -Aayush Aryan
date -04-11-2020
time -17:55
package -dictenory
Statement-Write a Python program to iterate over dictionaries using for loops

"""
class IterateDictionary:

    #create a method for iteration
    def iterate(self, dictOfNum):
        print("Dictionary : ", dictOfNum)
        for key, value in dictOfNum.items():
            print(key, " is the key belongs to " , dictOfNum[key])

dictionary = IterateDictionary()
rangeVal = int(input("Enter the length of dictionary : "))
dictOfNum = { }
for index in range(1, rangeVal + 1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

dictionary.iterate(dictOfNum)