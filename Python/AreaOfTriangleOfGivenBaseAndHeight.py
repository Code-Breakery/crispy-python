try:
	base = int(input('Enter base of ∆ : '))
	height =int(input('Enter height of ∆ : '))
	result = (1/2)*base*height
	print("AREA of ∆ = ",result)
except ValueError:
	print('please enter valid digit ')
