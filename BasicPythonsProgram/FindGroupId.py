"""
author - ${Aayush Aryan}
date - ${03-11-2020}
time - ${09:20am}
package - ${Basicpython}
Title -" Write a Python program to get the effective group id, effective user id, real group id, a list of
supplemental group ids associated with the current process.
Note: Availability: Unix."

"""
import os
try:
 print("\nEffective group id: ",os.getegid())
 print("Effective user id: ",os.geteuid())
 print("Real group id: ",os.getgid())
 print("List of supplemental group ids: ",os.getgroups())
 print()
except:
    print("checkedInbuiltMethodAndImportStatements")