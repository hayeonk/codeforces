from bisect import bisect
import sys

rl = lambda: sys.stdin.readline().split()
n = input()
A = map(int, rl())
q = input()

A = sorted(A)
D = sorted([A[i] - A[i-1] for i in xrange(1, n)])
P = [0] * n
for i in xrange(n-2, -1, -1):
	P[i] = P[i+1] + D[i]

ans = []
for _ in xrange(q):
	i, j = map(int, rl())
	diff = j - i
	idx = bisect(D, diff)
	hole = P[idx] - (diff + 1) * (n - idx - 1) 
	val = A[-1] - A[0] + diff - hole + 1
	ans.append(val)
print " ".join(map(str, ans))