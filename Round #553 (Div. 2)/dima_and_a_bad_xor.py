import sys
from itertools import product
rl = lambda: sys.stdin.readline().split()
n, m = map(int, rl())
A = [map(int, rl()) for _ in xrange(n)]
S = [set(row) for row in A]
ans = None
for col in product(*S):
	num = 0
	for c in col:
		num ^= c
	if num != 0:
		ans = col
		break
if not ans:
	print "NIE"
else:
	print "TAK"
	idx = []
	for i in xrange(n):
		idx.append(str(A[i].index(ans[i]) + 1))
	print " ".join(idx)