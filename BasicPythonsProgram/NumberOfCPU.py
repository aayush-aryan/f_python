"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${05:35pm}
package - ${Basicpython}

Title -" Write a Python program to find out the number of CPUs using."

"""
import multiprocessing
try:
 print(multiprocessing.cpu_count())
except:
    print("NumberOfCPU in the System is Undetermined")