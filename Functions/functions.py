#functions are used to break the entire code of the
#program into "modules" which may/may not take some data
#(called arguments) to produce a meaningful outcome

#functions are defined by "def" keyword

def addition(x,y):  #function declaration(x,y are arguments)
    return x+y      #function body

def subtraction(x,y):
    return x-y      #'return' is used to give back the produced
                    #output/data to the calling instruction
                    #alongwith the control

def multiplication(x,y):
    return x*y

def division(x,y):                  #function declaration
    if(not y):                      #function
        return 'Division undefined' #body
    return x/y

print('Enter two numbers:')
a,b=int(input()),int(input())
print('ADD: ',addition(a,b))
print('DIFFERENCE: ',subtraction(a,b))
print('PRODUCT: ',multiplication(a,b))
print('QUOTIENT: ',division(a,b))
