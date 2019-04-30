from collections import Counter
n = input()
A = map(int, raw_input().split())
A = Counter(A)
ans = []

if A[1] and A[2]:
	ans += [2, 1]
	A[1] -= 1
	A[2] -= 1

ans += [2] * A[2]
ans += [1] * A[1]
print " ".join(map(str, ans))