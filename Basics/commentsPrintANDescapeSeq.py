#comment, the print() function and escape sequences
#single line comment
'''Multiple
    line
    comment'''

#defination of print()
#print('String',value,sep=' ',end='\n',file=sys.stdout,flush=False)

#printing string(Hello World!!)
print('Hello World!!')
print('\n')

#printing integer values
print(35)
print('\n')

#printing integer values alongwith string
print('The year is',2019)
print('\n')

#print spanning multiple lines(in editor)
#statements/values in (),{} or []
print('The quick brown fox jumps over the lazy dog',
    'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed',
    'do eiusmod tempor incididunt')
print('\n')
#printing multiple lines in console
print('''
She's up all night 'til the sun
I'm up all night to get some
She's up all night for good fun
I'm up all night to get lucky

''')

#showing the role of 'sep' and 'end'
#sep is the character to be printed in between each of the valuse separated by commas
#end is the character to br printed at the end of the print values
print(1,2,3,4,sep='*')
print('is','4!','and is equal to',sep='\n',end='24\n')
print('\n')

#formatting print
#character followed by '%' in the string value acts as a placeholder
print('The year %d is not a leap year'%2019)    #Integer
print('The first letter of %s is %c'%('Python','P'))   #String alongwith character
print('%.3f'%23.44521)  #fractional number upto 3 decimal places
print('\n')

'''escape sequences use '\' to give new(or deactivate) functionality
    of any character after it'''
#some escape sequences may appear to not work in IDLE

#used escape sequence to display text properly
print('There\'s vomit on his sweater already: Mom\'s spaghetti')
#used escape sequence as alert
print('This thing rings a bell: \a')
#backspace
print('Everybody knows the bird is the word\b')
#newline
print('This is a line\nThis is a new line!')
#space
print('Gimme some space\sThere you go!')
#tab
print('Keeping tabs like\tthat')
#vertical tab
print('This is nothing\vbut tab rotated by 90 degrees :P')
#formfeed
print('Noticed\fanything?')
#carriage return
print('What does it\rdo?')
print('\n')

#used everything here
print('Defination of print():','print( \' String \' ,value,sep= \' \' ,end= \' \\ n \' ,file=sys.stdout,flush=False)',
      sep='\n',flush=True)