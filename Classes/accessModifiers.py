#access modifiers
'''python doesn't has any provision for access modifires like other OOP languages.
Instead the 'Name mangling' feature, alongwith some conventions can be used to
introduce semi-protected/semi-private features of any attribute of a class '''
class base():
    def __init__(self,a,x):
        self._pro = a       #'protected' attribute, leading single underscore
        self.__pri = x      #'private' attribute, leading double underscore
    def showdata(self):
        print('This object contains: Private',self.__pri,'and protected',self._pro)
    
class sub(base):
    def __init__(self,a,x):
        base.__init__(self,a,x)
        self.__pri = 15     #'private' attribute
    def afunc(self):
        print('This is from sub class')

Bvar = base(30,50)
Bvar.showdata()
#the 'protected' variable can still be accessed from outside
Bvar._pro = 70
Bvar.showdata()
'''however the name mangling feature converts the 'private' variable into
_className__variable, without the leading underscores, so it can't be
accessed/ modified as such'''
#Bvar.__pri = 15        #won't work
print(Bvar.__dict__)    #notice the 'private' variable as changed name
#but like the 'protected' variable, can be accessed from modified name
Bvar._base__pri=15
Bvar.showdata()
'''In case of inheritance, all variables, regardless of 'private' or
'protected', get inherited. Name mangling prevents overwriting of
inherited variables'''
Svar = sub(40,100)
print(Svar.__dict__)    #the base variables are a part of the sub class
Svar._base__pri = 110
print(Svar.__dict__)