n = input()
A = map(int, raw_input().split())
ret, v = A[n-1], A[n-1]-1
i = n-2
while i >= 0 and v >= 0:
	ret += min(A[i], v)
	v = min(A[i]-1, v-1)
	i -= 1
print ret