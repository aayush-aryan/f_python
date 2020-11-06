"""
author -Aayush Aryan
date -05-11-2020
time -12:55
package -dictenory
Statement-Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25
"""
class NumberSquaringDictionary :

    # create method for dictionar iteration
    def dictionary(self):

        """
               @param self: point 1
               @return: squaring value
               """
        number=int(input("Input a number "))
        Requireddictionary = dict()
        try:
            for indedx in range(1, number + 1):
                Requireddictionary[indedx]= indedx * indedx
                print(Requireddictionary)
        except KeyError :
            if __name__=='__main__':
               caller=NumberSquaringDictionary()
               caller.dictionary()