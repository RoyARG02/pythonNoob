#if-else is a way to bring some kind of logic
#to the program

'''if(some_expression):
        if "some_expression" is
        TRUE, then execute these
        statements
    else:
        if "some_expression" is
        FALSE, then execute these
        statements
'''
n=int(input('Enter a number: '))
if(n%2):
    print('Odd')
else:
    print('Even',end='\n\n')

#another layer of logic can be introduced by 'elif' before 'else'
'''if(some_expression):
        if "some_expression" is TRUE, then execute these
        statements
    elif(some_expression2):
        if "some_expression" is FALSE and some_expression2 is TRUE, 
        then execute these statements
    .
    .
    .
    else:
        if all expressions are FALSE, then execute these
        statements
'''
n=int(input('Enter a number: '))
if(n==0):
    print('Zero')
elif(n%2):
    print('Odd')
else:
    print('Even',end='\n\n')