#comprehensions
'''initializes any list/set/dictionary
with values satisfying any expression/iterable'''
#[<append this to list> <as long as this expression/iterable is running/true>]

odd20=[x for x in range (20) if (x%2!=0)]   #list comprehension
print(odd20)
pytha=[(x,y,z) for x in range(1,30)
                for y in range(x,30)
                for z in range(y,30)
                if(x*x+y*y==z*z)]           #another list comprehension
print(pytha)
squares={x:x**2 for x in range(15)}         #dictionary comprehension
print(squares)
uniqueChar={a for a in 'MISSISSIPPI'}       #set comprehension
print(uniqueChar)

#nested comprehensions
'''the initializer is itself another comprehension'''
some2D=[[j for j in range(5) if (j<=i)] for i in range(5)]
print(some2D)

'''in case of tuples, comprehension returns a generator'''
gen=(i for i in range(50) if(i%5==0))
print(gen)
for x in gen:
    print(x**2)