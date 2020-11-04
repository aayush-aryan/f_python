"""
author -Aayush Aryan
date -03-11-2020
time -17:25
package -Basicpython

Statement-Write a Python program to convert an integer to binary keep leading zeros.
Sample data : 50
Expected output : 00001100, 0000001100.

"""
def integerToBinaryConversion():
    try:
     sampleData = 50
     print(format(sampleData, '08b'))
     print(format(sampleData, '010b'))
    except :
        print("checkedSampleData")

integerToBinaryConversion()

