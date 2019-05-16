import sys
from collections import Counter
rl = lambda: sys.stdin.readline().split()
n, m = map(int, rl())

group = range(n)
rank = [1] * n

def find(u):
	if group[u] != u:
		group[u] = find(group[u])
	return group[u]

def union(u, v):
	u = find(u)
	v = find(v)
	
	if u == v:
		return 
	if rank[u] > rank[v]:
		u, v = v, u
	
	group[u] = v
	if rank[u] == rank[v]:
		rank[v] += 1

for _ in xrange(m):
	A = map(int, rl())[1:]
	for u in A:
		union(A[0]-1, u-1)
		
C = Counter([find(u) for u in xrange(n)])
ans = [C[find(u)] for u in xrange(n)]
print " ".join(map(str, ans))