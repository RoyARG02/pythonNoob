#indentation is very crucial in python for proper execution
#uncomment to see the error
n=int(input('Enter a number '))
'''
if(n<0):
print('Negative')   #IndentationError
else:
print('Positive')   #IndentationError
'''
#also the beginning of a suite should be denoted by
#adding a ':' at the end of the previous statement
'''
for i in range(4)   #SyntaxError
    print(i,end='')
'''