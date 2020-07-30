print('Hello, I am new to github! Nice to meet u')
while True:
	print('May I know your name ?')
	q = input('Y/N: ')
	if q == 'N':
		print('Ok, goodbye')
		break
	elif q != 'N' and q != 'Y':
		print('Your answer is invalid. Please try again!')
		continue
	else:
		a = input('Please input your name here: ')
		print('Hello %s, I am Werner'%a)
		break
