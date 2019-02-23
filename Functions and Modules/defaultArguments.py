#default arguments
'''arguments that a function takes(assumes) if
there is no information that is passed to it'''

def compliment(subject,adj='cool'):
    print('%s is %s'%(subject,adj))

compliment('Python')   #no second argument
compliment('Python','Modular')
compliment('C','not object oriented')
compliment('Java','Class based')