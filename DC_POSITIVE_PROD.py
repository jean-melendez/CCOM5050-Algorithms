def DC_POSITIVE_PROD(A, p, q):
	m = (p + q)//2
	if (p == q):
		if (A[p] >= 0):
			return A[p]
		else:
			return 1
	result = DC_POSITIVE_PROD(A,p,m) * DC_POSITIVE_PROD(A, m + 1, q)
A = [2, 0, -1, 7, -9, 0, 3, -20]
print(DC_POSITIVE_PROD(A,0, 1))