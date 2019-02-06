#operators: unary
#works on single operand
print(+5)   #operand: '5'
b=10
print(-b)   #operand: 'b'
print('')

#operators: arithmetic
print(4+6)  #addition
print(2-8)  #subtraction
print(3*9)  #multiplication
print(16/7) #division
print('')

print(5%2)  #remainder
print(4**3) #power(4^3)
print(10//3)    #round down after division(floor)
print('')

#operators: relational(evaluates to true or false)
print(0>14) #greater than
print(3<5)  #less than
print(4==(16/4))    #equals
print(10<=11)   #less than or equal to
print(1>=6) #greater than or equal to
print(2!=3) #not equals
print('')

#operators: logical(evaluates to true or false)
print(not 2)    #logical not
print((2>3)and(6<10))   #logical and
print((0!=1)or(4>10))   #logical or
print('')

#operators: assignment
a=2 #assigns 2 to 'a'
a=a+5   #computes 'a+5', and assigns result to 'a'
#assignment 'shorthands':
#the above statement can also be written as
a=2
a+=5
print(a)
print('')

b=10
b*=3    #b=b*3
print(b)    
b//=4   #b=b//4
print(b)
b**=2   #b=b**2
print(b)