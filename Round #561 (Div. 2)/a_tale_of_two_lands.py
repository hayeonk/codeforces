from bisect import *
n = input()
A = map(int, raw_input().split())
A = sorted([abs(x) for x in A])
ans = 0
for i in xrange(n):
	idx = bisect_right(A, 2 * A[i])
	ans += abs(idx - i - 1)
	
print ans