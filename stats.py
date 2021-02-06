import math
s = [88.2, 99.8, 88.8, 91.6, 92.9, 91.3, 90.4, 91.9, 95.6, 88.9, 90.1, 83.5, 87.7, 87.7, 88.0, 90.8, 83.9, 90.1, 91.4, 91.9, 93.7, 91.6, 87.6, 89.9, 91.1, 91.7, 90.1, 87.3, 93.8, 93.0, 87.7, 92.4, 88.3, 89.8, 89.1, 88.9, 91.1, 97.1, 89.7, 89.2, 88.9, 91.4, 88.3, 93.5, 90.9, 84.1, 92.7, 92.8, 90.7, 88.2, 95.0, 87.0, 90.3, 93.6, 89.9, 90.9, 91.5, 86.3, 90.6, 87.6, 88.5, 90.3, 89.8, 86.1, 89.6, 90.2, 93.2, 87.9, 93.3, 91.9, 92.8, 89.8, 100.4, 90.1, 93.1, 93.6, 89.3, 95.2, 91.2, 88.5, 89.7, 88.6, 85.7]
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


