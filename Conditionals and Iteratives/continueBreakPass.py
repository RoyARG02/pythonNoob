#break statement
'''skips any block of statements usually 
used in loops with if<condition>'''
for i in range(10):
    if(i==6):
        break   #skips and exits loop
    print(i,end=' ')
print('Exited loop')

#continue statement
'''skips block of statement for ONLY
THAT ITERATION which satisfies the condition
used with the statement'''
for i in range(10):
    if(i==4):
        continue   #skips to next iteration
    print(i,end=' ')
print('Exited loop')

#pass statement
'''essentially a NO OPERATION STATEMENT'''
for i in range(5):
    if(i==2):
        pass    #do nothing
    else:
        print('%d is not equal to 2'%i)
print('Exited Loop')