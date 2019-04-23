from fractions import gcd
n, m = map(int, raw_input().split())
A = map(int, raw_input().split())
P = map(int, raw_input().split())
g = A[1]-A[0]
for i in xrange(1, n):
	g = gcd(g, A[i]-A[i-1])

ans = -1
for i in xrange(m):
	if g % P[i] == 0:
		ans = i + 1
		break
if ans == -1:
	print "NO"
else:
	print "YES"
	print A[0], ans