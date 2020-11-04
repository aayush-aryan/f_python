"""
author -Aayush Aryan
date -04-11-2020
time -15:50
package -Basicpython

Statement-Write a Python function to find the maximum and minimum numbers from a sequence of
numbers.
Note: Do not use built-in functions.

"""
def findMaximumMinimumNumber(inputData):
    try:
     MaximumNumber = inputData[0]
     MinimumNumber = inputData[0]
     for number in inputData:
      if number> MaximumNumber:
        MaximumNumber = number
      elif number< MinimumNumber:
        MinimumNumber = number
    except:
        print("EnterValidargument")
    return MaximumNumber, MinimumNumber

print(findMaximumMinimumNumber([45, 25, 15, 91, -2, 42, 55, 28, 34]))