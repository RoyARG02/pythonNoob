#importing modules and identifiers
'''importing modules enables the use of scripts/functions defined in those modules
   equivalent to a "header file" in C/C++'''
#importing a module
import math
#this enables the use of functions defined in 'math' module in this script
print(math.sqrt(49))

#importing a specific func from module
from random import randint
print(randint(0,10))
#this also excludes the module name when calling the function

#importing a func by a new name
from keyword import kwlist as definedList
#this also works for the whole module as well
#import keyword as kw


'''identifiers are the names that the programmer gives to the user defined class/module/
   functions/memory locaions'''
#identifiers are case sensitive
#Apple is not same as apple or APPLE
'''the identifiers can include
   any alphanumeric characters (0-9),(a-z),(A-Z)
   underscore ( _ )'''
#the identifiers cannot include
# @ or ! or # or $ or % or any other special symbols
# a digit as the first character
# reserved keywords

print(definedList)
#this prints all the reserved keywords which cannot be identifiers

   


