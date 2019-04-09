from collections import Counter

n = input()
A = map(int, raw_input().split())

v, f = Counter(A).most_common(1)[0]
print n - f

idx = A.index(v)

for i in xrange(idx - 1, -1, -1):
	if A[i] != v:
		print 1 if A[i] < v else 2, i + 1, i + 2

for i in xrange(idx + 1, n):
	if A[i] != v:
		print 1 if A[i] < v else 2, i + 1, i