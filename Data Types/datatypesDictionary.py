#data types: Dictionary '{ : }'
#unordered set of data which can be referenced by a 'key'
#keys must be a single value, but values can be anything
exDict={'key1':'data1','key2':'data2','key3':'data3'}
androidDict={4:'Ice Cream Sandwich',5:'Lollipop',7:'Nougat'}

#dictionary values can be referenced the "same" way as lists
print(androidDict[7])   #instead, the "index" here is the key itself
print(exDict['key1'])

#adding to dictionaries
androidDict[9]='Pie'    #adding data "Pie" with key '9'
print(androidDict)

#modifying a value in dictionary
exDict['key2']=[2,5,7]
print(exDict)
print(exDict['key2'][2])    #accessed value in list

#removing a value in dictionary
del androidDict[4]  #used 'del' keyword
print(androidDict)