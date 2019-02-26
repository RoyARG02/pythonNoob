#constructors
'''constructors are basically initialization functions for
class data variables. It is defined using '__init__' keyword.
If not explicitly defined, python automatically creates one
with an empty body'''
class color:
    '''here no constructors are defined, python thus creates

    def __init__(self):
        pass
    '''
    def getColor(self,name):
        self.color=name
    def showColor(self):
        print(self.color)

class iceCream:
    '''here constructor is defined explicitly'''
    def __init__(self,name):
        self.flavour=name
    def taste(self):
        return self.flavour
    
myColor=color()
myColor.getColor('Blue')
myColor.showColor()
dessert=iceCream('Butterscotch')    #passed parameter to constructor
print(dessert.taste())