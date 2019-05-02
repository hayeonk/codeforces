import sys
n = input()
A = map(int, raw_input().split())
ans = 0
for i in xrange(1, n):
	if (A[i-1] == 2 and A[i] == 3) or (A[i-1] == 3 and A[i] == 2):
		print "Infinite"
		sys.exit()
	ans += A[i-1] + A[i]
	if i > 1 and A[i] == 2 and A[i-2] == 3:
		ans -= 1
print "Finite"
print ans