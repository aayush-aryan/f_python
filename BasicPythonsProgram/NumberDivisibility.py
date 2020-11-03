"""
author -Aayush Aryan
date -02-11-2020
time -11:45
package -Basicpython

Statement-Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function.

"""
def division():
    try:
      numberList = [300, 19, 30, 400, 100, 105, 75]
      resultList = list(filter(lambda x: (x % 15 == 0), numberList))
      print("Numbers divisible by 15 are", resultList)
    except:
        print("DivisionOccuredByOnlyPositiveNumber")

division()