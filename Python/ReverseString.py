#Unique way to reverse string
string = input('Input text : ')
reverse = ''
counter = -1
for char in string:
	reverse += string[counter]
	counter -=1
print(reverse)
	
	
	
	