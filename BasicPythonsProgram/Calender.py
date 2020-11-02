"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${12:05}
package - ${Basicpython}

Title -"  Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."

"""
import calendar
try:
 Year = int(input("enter the year in numeric form : "))
 Month = int(input("enter the month number in numeric form : "))
 print(calendar.month(Year, Month))
except:
    print("EnterValidYearAndMonth")