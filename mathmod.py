def prime_or_not(a):
	for i in range(2, a):
		if a%i == 0:
			return "not prime"
	else:
		return "prime"
		
def divisor(a):
	for i in range(1, a + 1):
		if a%i == 0:
			print(i)
			
def factorize(a):
	if prime_or_not(a) == "prime":
		print('%d is a prime number'%a)
	else:
		for i in range(2, a):
			if a%i == 0 and prime_or_not(i) == 'prime':
				k = 1
				while True:
					n = i**k
					m = i**(k + 1)
					if a%n == 0 and a%m != 0:
						print('%d^%d'%(i, k))
						break
					k = k + 1
					
def factorial(a):
	if a < 0 or a%1 != 0:
		print('Sorry, your number is invalid, please input a non-negative interger !')
	elif a == 0 or a == 1:
		return 1
	else:
		return a*factorial(a-1)
		
def fibonacci(a):
	if a <= 0 or type(a) != int:
		print('Sorry, your number is invalid, please input a non-negative interger !')
	elif a == 1 :
		return 0
	elif a == 2:
		return 1
	else:
		return fibonacci(a-1) + fibonacci(a - 2)
		
def sort_max(l):
	for i in range(len(l)-1, 0, -1):
		for k in range(i):
			if l[k] < l[k+1]:
				l[k], l[k+1] = l[k+1], l[k]

def sort_min(l):
	for i in range(len(l)-1, 0, -1):
		for k in range(i):
			if l[k] > l[k+1]:
				l[k], l[k+1] = l[k+1], l[k]
