#data types: tuples '( )'
#same as lists, but not mutable(can't be modified)
num=(1,2,3,4)
ch=('A','B','C','D','E')
#num[2]=5   doesn't work
#operators work similarly as on list
print(num*2)
print(num+ch)
print(num[0:2])

#data types: Sets   '{ }'
#same as lists, but has unique, NON-INDEXED elements
set1={1,2,3,4,4,6}
set2={'A','C','D','B'}
print(set1)
set2.add('D')   #inserting an element at the end of set
print(set2) #notice unordered arrangement