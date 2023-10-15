


def Incognito(A):
	n = A[0]
	y = 1
	i = 0
	j = 1
	while (i < n):
		x = A[i][0]
		while (j < n):
			if (A[i][j] > x):
				x = A[i][j]
		y = y * x
		i += 1	
	return y


rows, cols = (5, 5)
A = [[0]*cols]*rows
Incognito(A)