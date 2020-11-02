"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${06:50pm}
package - ${Basicpython}
Title -"Write a Python program to sort three integers without using conditional statements and
loops."
"""
try:
 FirstNumber = int(input("Enter first number: "))
 SecondNumber = int(input("Enter second number: "))
 ThirdNumber = int(input("Enter third number: "))

 LeastNumber = min(FirstNumber, SecondNumber, ThirdNumber)
 HeighestNumber = max(FirstNumber, SecondNumber, ThirdNumber)
 MiddleNumber = (FirstNumber + SecondNumber + ThirdNumber) - LeastNumber - HeighestNumber
 print("Sorted order Of Numbers are : ", LeastNumber, MiddleNumber, HeighestNumber)
except:
    print("EnterValidIntegerNumber")