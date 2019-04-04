import sys

rl = lambda: sys.stdin.readline().split()
n, m = map(int, rl())
A = map(int, rl())
S = [map(int, rl()) for _ in xrange(m)]
maxVal = -float('inf')
ans = []

def maximize_minimize(u, v):
	global maxVal
	global ans
	if u == v:
		if maxVal < 0:
			maxVal = 0
			return
	valMax, valMin = A[u], A[v]
	tmp = []
	for q, (i, j) in enumerate(S):
		if not (i-1 <= u <= j-1) and i-1 <= v <= j-1:
			tmp.append(q+1)
			valMin -= 1
	if maxVal < valMax - valMin:
		ans = [x for x in tmp]
		maxVal = valMax - valMin

for i in xrange(n):
	for j in xrange(n):
		maximize_minimize(i, j)
print maxVal
print len(ans)
print " ".join(map(str, ans))