import math

s = [17, 8, 17, 8, 13, 17, 13, 8]
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

standard = math.sqrt((totalSquare - ((total**2)/n))/(n-1))

print('standard deviation = ', standard)
print('mean = ', avg)
print('range = ', n)