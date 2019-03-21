#inheritance
#creating a new class from an existing class by inheriting the properties and methods
class Base():
    def __init__(self,X,Y):     #Base constructor
        self.dataA=X            #Base properties
        self.dataB=Y
    def showData(self):         #base method
        print('Data A:',self.dataA,'\nData B:',self.dataB)
    def __del__(self):          #base desctructor
        print('Base object destroyed.')

class Sub(Base):                #inherited Base to Sub
    def _init_(self,X,Y):       #Sub Constructor
        Base.__init__(self,X,Y) #Unlike other base methods, constructors are not inherited
                                #but invoked from the sub constructor

    def avgData(self):          #Sub Method
        print('Average data:',(self.dataA + self.dataB)/2)
    def __del__(self):          #sub destructor
        print('Sub class destroyed')

height = Sub(100,107.5)
height.showData()               #using inherited method
height.avgData()