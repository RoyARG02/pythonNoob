#classes
#blueprint of a data type which supports real-world behaviour
#contains some data and methods that work on that data
class twoValCalc:           #defination
    def getValue(self,x,y): #methods
        '''the methods defined in any class MUST HAVE AT LEAST ONE ARGUMENT 
        'self' at the beginning. The data variables of the class are referenced
         using that identifier'''
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y

user=twoValCalc()       #creating object
user.getValue(3,5)      #using methods
print(user.add())       #methods having only the 'self' argument
                        #don't require any parameters on call