#operator overloading
'''redefining an operator to function differently when used alongwith
an instance of a class
Overloading is done through special functions called 'magic methods'''

class complex():
    def __init__(self,x,y):
        self.real = x
        self.imag = y
    def __add__(self,arg):          #overloading the '+' operator(__add__ is the magic method)
        return complex(self.real + arg.real , self.imag + arg.imag)
    def  __eq__(self,arg):          #overloading the '==' operator(__eq__ is the magic method)
        if(self.real == arg.real and self.imag == arg.imag):
            return True
        else:
            return False
    def __gt__(self,arg):           #overloading the '>' operator(__gt__ is the magic method)
        if(self.real > arg.real):
            return True
        if(self.imag > arg.imag):
            return True
        else:
            return False
    def show(self):
        print(self.real,'+',self.imag,'\bi') 

obj1 = complex(2,3)
obj2 = complex(5,7)
obj3 = complex(7,10)
print('obj1 = ',end='')
obj1.show()
print('obj2 = ',end='')
obj2.show()
objRes = obj1 + obj2                #using overloaded operator
print('obj1 + ob2 = ',end='')
objRes.show()
print(obj1 > objRes)                #using overloaded operator
print(obj3 == objRes)               #using overloaded operator