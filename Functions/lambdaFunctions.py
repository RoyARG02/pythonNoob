#lambda functions
'''similar to anonymous functions that can take multiple
arguments but returns single value'''
#lambda <arguments>:<return value>
sum=lambda x,y: x+y
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
print('Sum of %d and %d is %d'%(a,b,sum(a,b)))