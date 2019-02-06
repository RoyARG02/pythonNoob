#operators: membership (evaluates to true or false)
colList=['Pink','Green','Blue','Violet','Black','Red']
print('Green' in colList)
print('black' in colList)   #case sensitive
print('Magenta' not in colList,end='\n\n')

#operators: identity (evaluates to true or false)
numList=[1,2,3]
exList=[]
a=20
b=a
exList=numList.copy()
print(a is b)
print(exList is not numList)    #due to lists being mutable