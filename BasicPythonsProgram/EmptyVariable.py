"""
author -Aayush Aryan
date -03-11-2020
time -14:50
package -Basicpython

Statement-Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}.

"""
def toCheckedEmptyVariable():
 n = 20
 try:
  d = {"x":200}
  print(type(n)())
  print(type(d)())
 except:
     print("EmptyVariableError")

toCheckedEmptyVariable()