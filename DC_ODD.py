def DC_ODD(A, p, q):
	m = (p + q)//2
	odd_pos = 0
	if (p == q):
		if (A[p] >= 0 and A[p] % 2 == 1):			
			odd_pos = odd_pos + 1			
			return odd_pos
		else:
			return 0
	result = DC_ODD(A,p,m) + DC_ODD(A, m + 1, q)	
	return result

A = [2, 0, -1, 7, -9, 0, 3, -20, 4]
B = [2, -7, 3, 0, 13, -1, 4, 0]
print(A)
print(B)
print(DC_ODD(A, 0, 8))
print(DC_ODD(A, 0, 7))