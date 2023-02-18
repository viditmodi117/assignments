# Write a Python program to convert a tuple to a string. 




def convertTuple(tup):
		
	str = ''
	for item in tup:
		str = str + item
	return str



tuple = ('k', 'n', 'o', 'w', 's')
str = convertTuple(tuple)
print(str)
