#random module
#defines methods needed for random operation
import random
someList=[2,3,'r',6,5,'M','Z',[0,7]]
print('choice(someList) =',random.choice(someList))  #returns any random element
random.shuffle(someList)    #shuffles elements of list
print(someList)
random.seed(100)    #starting value of generating random number
print('random() =',random.random())  #random float between 0 and 1(excluding)
print('randrange(0,10,2) =',random.randrange(0,10,2))
#returns a random value from a list having elements 
#starting from 0 and ending before 10; the difference between the 
#elements being 2 : [0,2,4,6,8] 
print('uniform(7,15) =',random.uniform(7,15)) #returns a float between 7 and 15
print('randint(10,50) =',random.randint(10,50)) #returns a number between 10 and 50