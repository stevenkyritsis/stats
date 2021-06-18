import math
s = [14, 6, 14, 6, 10, 14, 10, 6]
n = len(s)
s.sort()
total = 0
totalSquare = 0

if s == []:
	print('Please enter a list')

else:
	def median():
		m = int((n+1)/2)
		#print(type(m))
		print(s[m]) 

	#Mean
	for i in range(n):
		total = float(total + s[i])
	avg = total / n

	#Squared mean
	for i in range(n):
		totalSquare = (totalSquare + (s[i]**2))
	avgSquare = totalSquare / n

	#Variance
	vari = (totalSquare - ((total**2)/n))/(n-1)

	#Standard Deviation
	standard = math.sqrt(vari)

	#Range
	for i in range(n):
		maximum = max(s)
		minimum = min(s)

		ranges = maximum - minimum

	#Quartiles
	q1_position = int((n-1)/4)
	q1 = s[q1_position]


	q3_position = int((3*(n-1))/4)
	q3 = s[q3_position]

	q_range = q3 - q1

	#outliers
	out1 = q3 + q_range
	out2 = q1 - q_range
	outliers = []

	for j in range(n):
		if s[j] > out1 or s[j] < out2:
			outliers.append(s[j])

	print('list = ', s)
	print('Ammount = ', n)
	print('total = ', total)
	print('total squared = ', totalSquare)
	print('mean = ', avg)
	print('median = ', median())
	print('range = ', ranges)
	print('variance = ', vari)
	print('standard deviation = ', standard)
	print('Q1 = ', q1)
	print('Q3 = ', q3)
	print('Interquartile range = ', q_range)
	print('Outliers = ', outliers)


