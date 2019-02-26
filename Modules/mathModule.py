#math module
#defines mathematical and trigonometric functions
#also defines some mathematical constants

import math
print('sqrt(49) =',math.sqrt(49))   #square root
print('ceil(5.861) =',math.ceil(5.86))   #ceiling (round down)
print('floor(5.861) =',math.floor(5.86)) #floor (round up)
print('exp(2) =',math.exp(2))   #exponential (power as argument)
print('fabs(-5) =',math.fabs(-5))   #floating point abs value
print('log(10) =',math.log(10)) #natural log
print('log10(10) =',math.log10(10)) #log to the base 10
print('modf(5.861) =',math.modf(5.861)) #returns (<decimal part>,<integer part as float>)
print(math.pi)  #3.14159265...
print(math.e,end='\n\n')   #2.718...

print('sin(90) =',math.sin(90)) #argument is in radians
print('cos(pi/2) =',math.cos(math.pi/2))
print('tan(45) =',math.tan(45))
print('asin(1) =',math.asin(1)) #arc sine
print('acos(1) =',math.acos(1))
print('atan(1) =',math.atan(1))
print('atan2(3,2) =',math.atan2(3,2)) #equivalent to atan(3/2)
print('hypot(8,6) =',math.hypot(8,6))   # returns sqrt(8*8 + 6*6)
print('degrees(1) =',math.degrees(1))   #converts radians to degrees 
print('radians(30) =',math.radians(30)) #converts degrees to radians