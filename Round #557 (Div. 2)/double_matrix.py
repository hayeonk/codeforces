n, m = map(int, raw_input().split())
A = [map(int, raw_input().split()) for _ in xrange(n)]
B = [map(int, raw_input().split()) for _ in xrange(n)]

for i in xrange(n):
	for j in xrange(m):
		A[i][j], B[i][j] = max(A[i][j], B[i][j]), min(A[i][j], B[i][j])

def check(A):
	for i in xrange(n):
		for j in xrange(1, m):
			if A[i][j-1] >= A[i][j]:
				return False
	for i in xrange(1, n):
		for j in xrange(m):
			if A[i-1][j] >= A[i][j]:
				return False
	return True

if check(A) and check(B):
	print "Possible"
else:
	print "Impossible"