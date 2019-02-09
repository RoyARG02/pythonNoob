'''the syntax of the format() function is as follows
   {}.format(values)
where {} represents the placeholder sequence passed
to the print() function in the string, which need not be
in any specific order.
'Values' represent the actual data (be it of any data type)
to be placed in the placeholder identified by the index
from the left (starting from zero)
'''
print('{0} is {1} than {3} by {2}'.format(69,'greater',11,58))  #notice order
print('{2} is {0} than {3} by {1}'.format('greater',11,69,58))  #different order

#however, the function can only work with single string with
#which the function is "linked" to, in case there is any use of 
#commas in print()
print('{0} is {1}','than {2}','by {3}'.format(10,'lesser',21,11))
#in this case the format function has to written
#several times
print('{0} is {1}'.format(10,'lesser'),'than {0}'.format(21),
        'by {0}'.format(11))