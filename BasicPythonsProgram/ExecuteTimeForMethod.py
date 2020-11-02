"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${06:50pm}
package - ${Basicpython}
Title -"Write a program to get execution time for a Python method."

"""
import time
try:
 def SumOFNnumbers(number):
    startTime = time.time()
    sum = 0
    for index in range(1, number + 1):
        sum = sum + index
    endTime = time.time()
    return sum, endTime - startTime

 number = 10
except:
    print("provideIntegerNumber")
print("\n Time to sum of 1 to ", number," and required time to calculate :", SumOFNnumbers(number))