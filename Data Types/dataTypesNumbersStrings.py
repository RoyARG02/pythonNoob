#data types: Numbers
#Any numerical data(Integers,Float,Complex)

print(2,"is a (integer) number")
print(3.87,'is a (float)number')
print(2499866453878,'is a (long) number')
print(2+5j,'is a (complex) number')

#data types: Strings
#Any sequence of charactes enclosed in ' ' or " "

print('This is a string')
#used a var to store a string
str1='Hi! My name is '
str2="Slim Shady"
print('"',str1,'"','is another string')

#each character of the string is identified by an index
#similar to the elements of an array/list
#i.e., (0 to .....) or (..... to -1)
print(str2[2])  #prints the "2nd", or 3rd from left character
print(str1[-5]) #prints the "-5th", or 5th from right character

#slice operator in strings: gives a part of the string depending on the indices
print(str2[3:7])
#prints the "3rd,4th,5th and 6th" character of the string, stops at "7th"

#string repetation operator: prints string multiple times
print(str1*3)   #prints string 3 times

#string concatenation operator: joins two strings
print(str1+str2)
