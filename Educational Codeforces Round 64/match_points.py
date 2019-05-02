n, z = map(int, raw_input().split())
A = map(int, raw_input().split())
A.sort()
l, r = 0, n / 2
ans = 0
while l < n / 2 and r < n:
	if A[r] - A[l] >= z:
		ans += 1
		l += 1
	r += 1
print ans