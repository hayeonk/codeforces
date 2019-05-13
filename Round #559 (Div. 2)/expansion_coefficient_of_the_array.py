n = input()
A = map(int, raw_input().split())
ans = A[0] / (n - 1)
for i in xrange(1, n):
	ans = min(ans, A[i] / max(n-i-1, i))
print ans