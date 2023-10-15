import sys

def DQPow(a,b):
	if (b == 1):
		return a
	if (b == 0):
		return 1
	y = DQPow(a,b//2)
	if (b%2 == 1):
		y = y * y * a
	else:
		y = y * y
	return y

def Pow(x,m):
	if (x == 0 and m <= 0):
		print("Not defined")
	else:
		return DQPow(x,m)
	 

print(Pow(int(sys.argv[1]), int(sys.argv[2])))