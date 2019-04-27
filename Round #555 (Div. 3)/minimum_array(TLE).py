from bisect import bisect_left
from collections import Counter
n = input()
A = map(int, raw_input().split())
B = map(int, raw_input().split())
B = Counter(B)
ans = []
for num in A:
	l = sorted(B.keys())
	idx = bisect_left(l, n-num)
	if idx == len(l):
		idx = 0
	ans.append((num + l[idx])%n)
	B[l[idx]] -= 1
	if B[l[idx]] == 0:
		del B[l[idx]]
print " ".join(map(str, ans))