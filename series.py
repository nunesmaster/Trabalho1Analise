
import math

k = 1
i = 0
sol = 0

while i < 50:
	x = math.factorial(k)*math.factorial(k); 
	y = (k*k)*(math.factorial(2*k))

	sol = float(x)/y
	print sol

	# print sol
	i = i + 1
	k = k + 1

print 18 * sol
