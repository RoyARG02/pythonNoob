#class attributes
class Base1:
    "This is the base class 1"
    def nothing(self):
        print('Hello There!')

class Base2():
    "This is the Base Class 2"
    def __init__(self,X,Y):     
        self.dataA=X            
        self.dataB=Y
    def showData(self):        
        print('Data A:',self.dataA,'\nData B:',self.dataB)
    def __del__(self):         
        print('Base object destroyed.')

class Sub(Base1,Base2):          #Multiple Inheritance
    "This is the inherited Sub Class"                
    def _init_(self,X,Y):       
        Base2.__init__(self,X,Y) 
    def avgData(self):          
        print('Average data:',(self.dataA + self.dataB)/2)
    def __del__(self):         
        print('Sub class destroyed')

height = Sub(100,107.5)
height.nothing()              
print('height.__dict__:',height.__dict__)   #dictionary containing the variables having class' namespace
print('height.__doc__:',height.__doc__)     #documentation string of the class
print('Sub.__name__:',Sub.__name__)        #name of the class(doesn't work on instances)
print('height.__module__:',height.__module__)   #module where the class is defined. Default is '__main__'
print('Sub.__bases__:',Sub.__bases__)       #tuple containing the names of the super class(or classes)