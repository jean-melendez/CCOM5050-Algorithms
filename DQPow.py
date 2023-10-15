import sys

def DQPow(x,m):
	if (m == 1):
		return x
	if (m == 0):
		return 1
	y = DQPow(x,m//2)
	if (m%2 == 1):
		y = y * y * x
	else:
		y = y * y
	return y
	 

print(DQPow(int(sys.argv[1]), int(sys.argv[2])))