from collections import defaultdict
n = input()
A = map(int, raw_input().split())
i, j = 0, n-1
while A[i] == A[n-1]:
	i += 1
while A[0] == A[j]:
	j -= 1
print max(n - i - 1, j)