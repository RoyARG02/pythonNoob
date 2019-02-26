#destructors
'''functions that execute when an object of a class
or the program itself is removed from memory
defined by '__del__' keyword'''
class justSample:
    def __init__(self):
        print('Object Created')
    def someMethod(self,take):
        print('This object has a value equal to',take)
    def __del__(self):
        print('Object Deleted')

anObj=justSample()
anObj.someMethod('wait what?')
pie=justSample()
pie.someMethod(22/7)
del pie                 #explicitly deleted the object
print('End of program')