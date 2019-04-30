import sys
rl = lambda: sys.stdin.readline().split()

n, q = map(int, rl())
S = raw_input().strip()
R = [[] for _ in xrange(3)]

def check(i, j, k, idx, m):
	if i >= len(R[0]) and j >= len(R[1]) and k >= len(R[2]):
		return True
	if idx >= n:
		return False
	if (i, j, k, idx) in m:
		return m[(i, j, k, idx)]
	if i < len(R[0]) and R[0][i] == S[idx]:
		if check(i+1, j, k, idx+1, m):
			m[(i, j, k, idx)] = True
			return True
	if j < len(R[1]) and R[1][j] == S[idx]:
		if check(i, j+1, k, idx+1, m):
			m[(i, j, k, idx)] = True
			return True
	if k < len(R[2]) and R[2][k] == S[idx]:
		if check(i, j, k+1, idx+1, m):
			m[(i, j, k, idx)] = True
			return True
	for c in xrange(idx+1, n):
		if check(i, j, k, c, m):
			m[(i, j, k, idx)] = True
			return True
	m[(i, j, k, idx)] = False
	return False
	
for _ in xrange(q):
	i = rl()
	if i[0] == "+":
		s, num, r = i
	else:
		s, num = i
	num = int(num)-1
	if s == "+":
		R[num].append(r)
	else:
		R[num].pop()
	if check(0, 0, 0, 0, {}):
		print "YES"
	else:
		print "NO"