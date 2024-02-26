
def NutsandBolts(A,B):
	tmp = 0
	j = 0
	jSum = 0
	last = len(B) - 1
	while (len(A) > 0):

		if A[0] == B[j]:
			tmp = B[j]
			print("found match in i:", A[0], " == j:", B[j])
			B[j] = B[last]
			B[last] = tmp
			jSum += j
			print("jSum = ", jSum)
			j = 0
			last -= 1
			print("j = ", j)
			A.pop(0)

		else:
			j += 1
			print("j = ", j)
	print(B)
	return A


def NutsandBoltsOrig(A,B):

  j = 0
  jSum = 0
  while (len(A) > 0):
   
      if A[0] == B[j]:
        print("found match in i:", A[0], " == j:", B[j])
        jSum += j
        print("xSum = ", jSum)
        j = 0
        A.pop(0)
      else:
        j += 1
        print("x = ", j)

  return A


A = [1,2,3,9,5,4,6]
B = [1,3,2,5,4,9,6]

#print(NutsandBolts(A,B))
		
C = [5,6, 8, 90, 4, 3]
D= [6, 90, 8, 5, 4, 3]

#print(NutsandBolts(C,D))

G = [1,2,3,4,5,6,7,24,8,9,0,40,10,11,12,13,14,15,21]
F= [10,21,15,40,14,13,12,11,0,1,8,9,6,3,2,5,7,4,24]

#print(NutsandBolts(G,F))
#print(NutsandBoltsOrig(G,F))

Y = [1,2,3,4,5,6,7,8,9]
Z= [9,8,7,6,5,4,3,2,1]

#print(NutsandBolts(Y,Z))
#print(NutsandBoltsOrig(Y,Z))

R = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
T = [17,5,24,6,19,16,21,8,13,30,1,25,28,15,20,29,3,9,4,23,11,10,18,7,26,14,12,2,27,22]

#print(NutsandBolts(R,T))
#print(NutsandBoltsOrig(R,T))

V = [21, 11, 16, 22, 6, 9, 12, 2, 20, 15, 14, 23, 10, 24, 8, 13, 17, 5, 4, 7, 19, 18, 1, 25, 3]
W = [9, 6, 21, 25, 18, 13, 3, 2, 14, 23, 11, 1, 17, 20, 8, 7, 15, 16, 12, 19, 24, 5, 22, 10, 4]

#print(NutsandBolts(V,W))
#print(NutsandBoltsOrig(V,W))

S = [38,19,37,45,15,5,22,42,36,4,46,10,9,2,32,34,30,26,3,41,14,28,20,1,43,17,31,44,11,35,39,18,7,33,29,13,27,24,16,40,49,47,8,6,12,48,21,25,23,50]
K = [7,45,14,40,35,46,30,20,29,32,48,17,16,9,28,44,33,47,37,24,23,42,12,38,4,3,25,36,5,11,19,6,39,2,50,10,21,13,1,26,15,43,31,18,8,22,34,27,41,49]

print(NutsandBolts(S,K))
#print(NutsandBoltsOrig(S,K))