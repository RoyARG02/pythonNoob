#so suppose you create a function that
#changes the value of a "global" variable like

#Uncomment to see the error
'''
def increVar():
    var+=1

var=int(input('Enter a integer '))
increVar()
print(var)
'''

#This will give an error of an unrefernced variable
#as python will assume that the 'var' in the function
#is a new local variable which masks the "global" variable

#a workaround solution is to pass the "global" variable
#as a argument to the function (and return the value as
#the change is required)

def changeVar(var):
    return var+1

var=int(input('Enter a integer '))
var=changeVar(var)
print(var)
