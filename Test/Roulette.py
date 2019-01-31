from random import randint as rand

def spin():
    print('Spinning...')
    return rand(0,6)

def fire(bullet):
    return bullet-1

print('Russian roulette simulator')
bullet=0
survive=0
print('Loading and',end=' ')
bullet=spin()
while True:
    opt=input('Press Y to fire, any key to spin again: ')
    if(opt=='y' or opt=='Y'):
        bullet=fire(bullet)
        if(bullet>=0):
            print('Blank!!!')
            survive+=1
        else:
            print('Shot!!')
            print('Survived %d shots'%survive)
            survive=0
            print('Loading again and',end=' ')
    bullet=spin()
    
