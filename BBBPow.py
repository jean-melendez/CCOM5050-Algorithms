import sys

def BBBPow(x,m):
	n = m 
	y = 1
	z = x
	while(n != 0):
		r = n%2
		if (r == 1):
			y = y*z
		z  = z*z
		n = n//2
	return y

print(BBBPow(int(sys.argv[1]), int(sys.argv[2])))