#method overriding
'''defining a function with the same name, arguments and return
type in a sub class overrides the function inherited from the
base class '''

class parent():
    def __init__(self,str):
        self.str = str
    def show(self):
        print('The no. of characters in %s is %d' %(self.str,len(self.str)))
    def __del__(self):
        print('Parent Class destroyed')
    
class child(parent):
    def __init__(self,str,index):
        parent.__init__(self,str)
        self.index = index
    def show(self):             #overriding
        print('The object has:',self.str)
        print('The string after first %d characters is:%s' %(self.index, self.str[self.index : ]))
    def __del__(self):          #overriding
        print('Even the functions like __init__() or __del__() can be overridden')

anObj = child('Python is fun!',5)
anObj.show()                    #the child function is invoked