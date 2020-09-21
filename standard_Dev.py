import math

s = [1.61, 1.94, 2.62, 2.37, 3.09, 3.20, 2.53, 1.89]
n = len(s)
total = 0
totalSquare = 0

#Mean
for i in range(n):
	total = total + s[i]
avg = total / n

#Squared mean
for i in range(n):
	totalSquare = (totalSquare + (s[i]**2))
avgSquare = totalSquare / n

#Variance
vari = (totalSquare - ((total**2)/n))/(n-1)

#Standard Deviation
standard = math.sqrt(vari)

print('mean = ', avg)
print('range = ', n)
print('variance = ', vari)
print('standard deviation = ', standard)