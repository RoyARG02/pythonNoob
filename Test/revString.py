def reverse(string):
    if(len(string)==0):
        return ''
    else:
        reverse(string[1:])
        if(string[:1].isupper()and string[1:2]!=' '):
            print(string[:1].lower(),end='')
        elif(string[:1].islower() and string[1:2]==' '):
            print(string[:1].upper(),end='')
        else:
            print(string[:1],end='')

strInput=input('Enter any sentence: ')
reverse(strInput+' ')
