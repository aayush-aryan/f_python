"""
author - ${Aayush Aryan}
date - ${02-11-2020}
time - ${07:28pm}
package - ${Basicpython}
Title -" Write a Python program to find the available built-in modules."
"""

import sys
import textwrap
try:
 module_name = ', '.join(sorted(sys.builtin_module_names))
 print(textwrap.fill(module_name, width=70))
except:
    print("CheckedInBuiltMethodAndArgument")