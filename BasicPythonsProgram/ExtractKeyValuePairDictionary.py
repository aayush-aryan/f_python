"""
author -Aayush Aryan
date -03-11-2020
time -16:50
package -Basicpython

Statement-Write a Python program to extract single key-value pair of a dictionary in variables..

"""
def extractKeyValue():
    try:
     givenDictionary = {'Aayush': 'Aryan'}
     (dict1, dict2), = givenDictionary.items()
    except:
        print("DefineProperDictionary")
    print(dict1)
    print(dict2)
extractKeyValue()    
