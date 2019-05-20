from collections import Counter
n = input()
C = Counter()
for _ in xrange(n):
	C[raw_input()[0]] += 1

def countPair(n):
	return n * (n-1) / 2

ans = 0
for c in C:
	ans += countPair(C[c] / 2)
	ans += countPair(C[c] / 2 + (C[c]%2))
print ans
	