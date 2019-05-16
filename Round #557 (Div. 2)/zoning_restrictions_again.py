n, h, m = map(int, raw_input().split())
A = [h] * n
for _ in xrange(m):
	l, r, x = map(int, raw_input().split())
	for i in xrange(l-1, r):
		A[i] = min(A[i], x)

print sum([h*h for h in A])