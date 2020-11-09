"""
author -Aayush aryan
date -07-11-2020
time -13:15
package -List
problem Statement-Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""

class SortedList:

  def last(number):
      return number[-1]

def last(args):
    pass

def sortListLast(tuples):
     try:
        return sorted(tuples,key=last)
        print(sortListLast([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
     except:
         print("EnterValidEntry")

if __name__ == "__main__":
       sortedList = SortedList()
       sortedList.sortListLast()