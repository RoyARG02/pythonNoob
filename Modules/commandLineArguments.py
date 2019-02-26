#command line arguments
#argumets which can be supplied to the program at runtime
from sys import argv
'''arguments reside in the 'argv' list which is a part of
'sys' module

argv list generally contains the location of the source code
file supplied to python as its first element
'''

def workWithArgs(arguments):
    for i in arguments:
        print('Argument',arguments.index(i),'->',i)    #this lists the arguments supplied to the program

print('The list of arguments supplied are:')
workWithArgs(argv)