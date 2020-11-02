"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${1:30}
package - ${Basicpython}

Title -" Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"

"""
from datetime import date
try:
 FirstDate = date(2014, 7, 2)
 LastDate = date(2014, 7, 11)
 NumberOfDays = LastDate - FirstDate
 print(NumberOfDays.days)
except:
 print("EnterValidDateFormat")