"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${2:30}
package - ${Basicpython}

Title -" Write a Python program to create a histogram from a given list of integers."

"""
try:
 def histogram(listOfInteger):
    for number in listOfInteger :
        output = ''
        temVariable = number
        while(temVariable > 0):
          output = output + '*'
          temVariable = temVariable - 1
        print(output)

 histogram([2, 3, 6, 5])
except:
    print("InvalidEntryOfItems")