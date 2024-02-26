def PartitionEvenOdd(A):
	pos = 0
	while (pos < len(A)):
		impar = pos 
		for i in range(len(A)):
			if (A[i] % 2 == 1):
				impar = i
				break
		print("Pos de primer # impar: ", impar)

		if (A[pos] % 2 == 0):
			A[pos], A[impar] = A[impar], A[pos]
		print("Arreglo: ", A)

		pos += 1

	return A 

A = [1,2,3,4,5,6,7]
PartitionEvenOdd(A)
print(A)

B = [1,2,3,4,5,6,72,8,9,71]
PartitionEvenOdd(B)
print(B)