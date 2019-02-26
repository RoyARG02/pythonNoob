#return multiple values
'''returning multiple valuse is easy.
Just separate the multiple values by commas'''

def swap(x,y):
    x,y=y,x     #swapping values(MIND = BLOWN)
    return x,y

a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
print('Values before swapping:','a = %d'%a,'b = %d'%b,sep='\n')
a,b=swap(a,b)
print('Values after swapping:','a = %d'%a,'b = %d'%b,sep='\n')