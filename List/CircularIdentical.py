"""
author -aayush aryan
date -08-11-2020
time -11:15
package -List
problem Statement-Write a python program to check whether two lists are circularly identical.
"""

from List.UtilityPackage import Ulility
class CircularIdentical:
    def circularly_identical(self,list1, list2,list3):

        """
        # function to check circularly identical or not
        :param list1:
        :param list2:
        :param list3:
        """
        print('Compare list1 and list2')
        print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
        print('Compare list1 and list3')
        print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


if __name__ == '__main__':
    list1=Ulility.createList()
    list2=Ulility.createList()
    list3=Ulility.createList()

circular=CircularIdentical()
circular.circularly_identical(list1, list2, list3)