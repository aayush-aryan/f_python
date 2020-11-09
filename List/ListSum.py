"""
author -aayush aryan
date -07-11-2020
time -02:07
package -List
problem Statement-'Write a Python program to sum all the items in a list.'
"""


class ListSum(object):
    pass

class ListSum:
 def sum_list(items):
     """
     :param items:
     :return:
     """
     sum_numbers = 0
     for x in items:
         sum_numbers += x
     return sum_numbers
 print(sum_list([40,12,11]))

 if __name__ == "__main__":
     listData = ListSum()
     listData.Sum_list()