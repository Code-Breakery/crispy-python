bin = ''
binV = bin.split(" ")
text = ''
for bins in binV:
	integer = int(bins,2)
	String = chr(integer)
	text += String
print(text)