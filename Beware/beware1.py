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
print('var after changeVar() =', var)

#the 'global' keyword can also be used to denote the global variable
#this also works for nested functions
#'global' is not required if the variable is being accessed ONLY

def changeGlob():
    x = 15
    def nestedGlob():
        global var      #out of scope variable 'var' used here
        var += x        #'x' is only being accessed, thus no 'global' required
        print('var in nestedGlob() =', var)
    nestedGlob()

changeGlob()
