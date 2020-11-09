"""
author -aayush aryan
date -08-11-2020
time -9:30
package -List
problem Statement-'Write a Python program to get the difference between the two lists.'
"""


class ListDifference :

 def diffOfList(self):
     try:
       list1 = [1, 3, 5, 7, 9]
       list2=[1, 2, 4, 6, 7, 8]
       diff_list1_list2 = list(set(list1) - set(list2))
       diff_list2_list1 = list(set(list2) - set(list1))
       total_diff = diff_list1_list2 + diff_list2_list1
       print(total_diff)
     except:
         print("InvalidListElement")

if __name__ == '__main__':
    copyList=ListDifference()
    copyList.diffOfList()