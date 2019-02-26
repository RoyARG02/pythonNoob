#Variable Argumnets
'''variable(extra) arguments to a function becomes
an element of a tuple signified with a '*' symbol'''

def avg(x,y,*var):
    print('Variable Arguments:',var)
    if(len(var)==0):
        return (x+y)/2
    else:
        varSum=0
        for i in var:
            varSum+=i
        return (x+y+varSum)/(len(var)+2)

print('avg(15,17):',avg(15,17))
print('avg(1,2,3,4,5,6,7,8):',avg(1,2,3,4,5,6,7,8))
print('avg(12,88,57,32):',avg(12,88,57,32))