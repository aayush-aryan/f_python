"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${07:39pm}
package - ${Basicpython}
Title -"Write a Python program to get the size of an object in bytes."
"""
import sys
FirstString = "Java"
SecondString = "Python"
ThirdString = "ShellScript"
print()
try:
 print("Memory size of '" + FirstString + "' = " + str(sys.getsizeof(FirstString)) + " bytes")
 print("Memory size of '" + SecondString + "' = " + str(sys.getsizeof(SecondString)) + " bytes")
 print("Memory size of '" + ThirdString + "' = " + str(sys.getsizeof(ThirdString)) + " bytes")
 print()
except:
    print("ProvideProperObjectAndCheckedInBuiltMethod")
