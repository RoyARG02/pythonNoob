str="SKRATTA DU FORLORAR DU"
print(len(str))
for i in range(len(str)):
	for k in range(int(len(str))-i):
		print(' ',end='')
	for j in range(i+1):
		print(str[j],end=' ')
	print('\n')
