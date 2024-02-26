#n = 4 # there are four nodes in example graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using 
# all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
	0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

dist2 = [[0, 0, 0, 0, 0], [0, 0, 25, 30, 20], [
	0, 13, 8, 2, 2], [0, 15, 5, 1, 30], [0, 2, 15, 35, 0]]

dist3 = [[0, 0, 0, 0], [0, 13, 8, 2], [0, 15, 5, 30], [0, 2, 15, 0]]

dist4 = [[0, 0, 0, 0, 0], [0, 4, 56, 7, 9], [0, 21, 45, 57, 22], [0, 9, 12, 3, 7], [0, 45, 9, 8, 0]]

dist5 = [[0, 0, 0, 0, 0, 0], [0, 4, 5, 5, 7, 9], [0, 1, 2,  4, 7, 2], [0, 1, 12, 4, 3, 7], [0, 9, 5, 2, 8, 0], [0, 5, 3, 4, 8, 0]]

dist6 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 25, 7, 4, 30, 20], [0, 13, 23, 6, 8, 2, 2], [0, 15, 4, 7 , 7, 1, 30], [0, 2, 5, 2, 15, 35, 0],
[0, 3, 6, 7, 2, 6, 8], [0, 8, 3, 5, 1, 12, 0]]

def node_calc(mat):
	n = len(mat) - 1
	return n

n = node_calc(dist)

n2 = node_calc(dist2)

n3 = node_calc(dist3)

n4 = node_calc(dist4)

n5 = node_calc(dist5)

n6 = node_calc(dist6)


def fun(i, mask):
	# base case
	# if only ith bit and 1st bit is set in our mask,
	# it implies we have visited all other nodes already

	#n = node_calc(dist)
	global mat
	#print(len(mat))
	n =  len(mat) - 1

	memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]

	if mask == ((1 << i) | 3):
		return mat[1][i]

	# memoization
	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 100000000000 # initial high value to ensure lowest costs are calculated

	# we have to travel all nodes j in mask and end the path at ith node
	# so for every node j in mask, recursively calculate cost of 
	# travelling all nodes in mask
	# except i and then travel back from node j to node i taking 
	# the shortest path take the minimum of all possible j nodes
	for j in range(1, n+1):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + mat[j][i])
	memo[i][mask] = res # storing the minimum value
	return res

def ans(n, matrix):	

	global mat
	mat = matrix
	# Driver program to test above logic
	ans = 100000000000
	for i in range(1, n+1):
		# try to go from node 1 visiting all nodes in between to i
		# then return from i taking the shortest route to 1
		ans = min(ans, fun(i, (1 << (n+1))-1) + matrix[i][1])

	print("The cost of most efficient tour = " + str(ans))


ans(n,dist)
ans(n2,dist2)
ans(n3,dist3)
ans(n4, dist4)
ans(n5, dist5)
ans(n6, dist6)