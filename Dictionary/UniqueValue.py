"""
author -Aayush Aryan
date -05-11-2020
time -12:55
package -dictenory
Statement-Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

class UniqueValueDictionary:

    def unique(self, dictionarySet):
        """
                     @ This method printing unique value
                     @param dictionarySet: this is use for dictionat value
                     @return: Remove the repeating value
                     """
        print("Dictionary : ", dictionarySet)
        uniqueValue = set(val for dict in dictionarySet for val in dict.values())
        print("Unique Dictionary: ", uniqueValue)
dictValue = UniqueValueDictionary()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = {}
for index in range(1, rangeVal + 1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

dictSet = [dictOfNum]
print(dictSet)
dictValue.unique(dictSet)