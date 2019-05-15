from collections import defaultdict
n = input()
A = map(int, raw_input().split())
B = map(int, raw_input().split())
mod = 998244353 

for i in xrange(n):
	left = i + 1
	right = n - i
	A[i] *= left * right
	
d = defaultdict(list)
for n1, n2 in zip(sorted(A), sorted(B, reverse=True)):
	d[n1].append(n2)

ans = 0
for n in A:
	ans = (ans + n * d[n].pop()) % mod
print ans