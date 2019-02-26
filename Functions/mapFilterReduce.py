#map(<function>,<list/iterable>)
'''creates a new object by taking an element from
existing list and applying some function'''
sampleList=[0,1,2,3,4,5,6,7,8,9]
squareList=list(map(lambda x:x**2,sampleList))  #converting to list
print(squareList)

#filter(<function>,<list/iterable>)
'''creates a new object by taking an element from
existing list and applying a function and adding it
if the function evaluates to true'''
evenList=list(filter(lambda x:(x%2==0),sampleList)) #converting to list
print(evenList)

#reduce(<function>,<list/iterable>)
'''returns an expression by taking an element from existing list 
and continually (this element and the next element consecutively)
applying a function'''
from functools import reduce
cumulativeSum=reduce(lambda x,y: x+y,sampleList)
print(cumulativeSum)