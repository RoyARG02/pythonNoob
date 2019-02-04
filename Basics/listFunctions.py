#some useful functions used in lists
charList=['A','B','C','D']
numList=[1,2,3,4]
print('len()',len(numList)) #length of list
print('max()',max(charList))    #maximum element of list
print('min()',min(charList))    #minimum element of list
exTuple=(7,8,9)
print('list()',list(exTuple))    #converts Tuple to List
charList.append('B')    #inserts element at end
print('list.append()',charList)
print('list.count()',charList.count('B'))  #frequency of given element
charList.remove('B')    #removes the given element from list
#in case of multiple elements, removes the first element from left
print('list.remove()',charList)
print('list.index()',numList.index(3)) #gives index of the given element
numList.sort()  #sorts the elements (ascending), elements must be of same datatype
print('list.sort()',numList)
charList.sort(reverse=True) ##sorts the elements (desecnding)
print('list.sort(reverse=True)',charList)
numList.extend(charList)    #concatenates two lists (similar to '+')
print('list.extend()',numList)
numList.reverse()   #reverses elements of a list
print('list.reverse()',numList)
charList.insert(2,222)  #inserts given ELEMENT(222), at the given INDEX(2)
print('list.insert()',charList)
charList.pop()  #removes the last element
print('list.pop()',charList)
numList.clear() #removes all elements
print('list.clear()',numList)
numList=charList.copy() #gives a copy
print('list.copy() and finally',numList)
print(charList)