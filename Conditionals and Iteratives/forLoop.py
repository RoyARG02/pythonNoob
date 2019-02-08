#for loop: for executing statements for a specific number
#of time

#generally iterates over a list
samplelist=['A','Apple','B','Ball','C','Cat','D','Dog','E','E']
for i in samplelist:
    print(i,end=' ')
print('')

#using the range() function
for i in range(10): #range(start,stop,step)
    print(i,end=' ')
print('')

for j in range(1,15,3):
    print(j,end=' ')
print('')

#else statement in for loop
for i in range(0,10,2):
    print('i is',i)
else:
    print('Exited for')     #statement will be executed
                            #when for is finished