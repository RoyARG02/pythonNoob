#while loop: for statements which need to be executed
#as long as a condition is true

i=0     #initializing
while i<10:    #while <condition>
    print(i,end=' ')    #statements will be executed as
    i+=1                #long as condition is true
print('')

#else statement in while loop
i=0
while i<15:
    print('i is',i)
    i+=2
else:
    print('Exited while')   #statement will be executed when
                            #while is finished
#infinite loop(Uncomment)
'''
while True:
    print('Infinite')
'''