#data types: lists  '[ ]'
'''unordered collection of data of any type
that can be modified(mutable)'''
num=[1,2,3,4] #list containing only numbers
ch=['A','B','C','D','E']    #list containing only characters
list1=[1,4,'AB',2+3j,"Pie",'t'] #list containing different types of data
ch[3]='Z'   #modifying list using index
print(ch)

'''A list having lists inside it can be called
as a multi dimensional list'''
Mult=[[2,6],[7,9]]  #2X2 multi dimensional list
Mult2=[[2,[3,4],[4,78]],[11,[4,5]]] #another multi dimensional list
'''for readability, the above list can also be written as
Mult2=[
    [2,[3,4],[4,78]],
    [11,[4,5]]
    ]
'''
#some operators for lists (similar to strings)
#repeatation operator
print(ch*2)

#concatenation operator
print(num+ch)

#slice operator
print(list1[1:4])
print(list1[2:])    #absence of index means till end/from beginning