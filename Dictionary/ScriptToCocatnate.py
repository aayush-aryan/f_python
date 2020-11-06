"""
author -Aayush Aryan
date -05-11-2020
time -12:55
package -dictenory
Statement-Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
class AddKeyToDict:
    def addKey(self, dictOfNum,key,value):
        print(dictOfNum)
        dictOfNum.update({key: value})
        print(dictOfNum)
'''
    @param self:
    @param dictOfNum:
    @param key:
    @param value:
    @return:
    '''
dictionary = AddKeyToDict()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for index in range(1, rangeVal + 1):
    val = int(input("Enter The value for dictionary : "))
    dictOfNum.setdefault(index, val)
key = int(input("Enter The Key In Which You Want To Add The Value : "))
value = int(input("Enter The Value : "))
dictionary.addKey(dictOfNum,key,value)


