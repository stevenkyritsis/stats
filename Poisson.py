import math

#This is for Poisson Distribution where where the probability that there are 3 or less errors in 100 pages where lamda is 0.03

def poisson(lamda, num):
	result1  = ((math.exp(-lamda) * (lamda**num))/math.factorial(num))
	return result1

def less_than():
	x = int(input('please enter your x: '))
	new_lamda = float(input('Please enter your lamda: '))

	result2 = 0
	for i in range(x+1):
		result2 += poisson(new_lamda, i)
	return result2

def greater_than():
	result3 = 1 - less_than()
	return result3

user = 0

while user != 4:
	print('1. P(X=x)\n')
	print('2. P(X<x)\n')
	print('3. P(X>x)\n')
	print('4. Exit\n')
	user = int(input('Please enter one of the following options for Poisson Distribution.\n'))

	if user == 1:
		user_lamda = float(input('Please enter your lamda: '))
		user_x = int(input('Please enter your x: '))
		print(poisson(user_lamda, user_x))
	elif user == 2:
		print(less_than())
	elif user == 3:
		print(greater_than())
	elif user == 4:
		print('Exiting program...')
	else:
		print('Please enter one of the following options.\n')
