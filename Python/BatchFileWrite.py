import os
path = input('Input dir path : ')
ext = input('Input file extension that you want to write : ')
text = input('Input text that you want to write: ')
counter= 0

for file in os.listdir(path):
	splitName = file.split('.')[-1]
	if splitName == ext:
		counter += 1
		with open(path+file,'a') as f:
			f.write(text)
			
print('%d File(s) writed '%counter)
		