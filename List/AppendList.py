"""
author -aayush-aryan
date -08-11-2020
time -15:36
package -List
problem Statement-'Write a Python program to append a list to the second list.'
"""
class AppendList:
    def listAppend(self):
        try:
          list1 = [4, 5, 6, 7]
          list2 = ['aayush', 'aryan', 'singh']
          final_list = list1 + list2
          print(final_list)
        except :
            print("ListInputError")
if __name__ == '__main__':
    appemdlist=AppendList()
    appemdlist.listAppend()