import sys
rl = lambda: sys.stdin.readline().split()
n = input()
A = [map(int, rl()) for _ in xrange(n)]
def compare(n1, n2):
	a1, b1 = n1
	a2, b2 = n2
	first = a1 + 2 * b1 + 2 * a2 + b2
	second = 2 * a1 + b1 + a2 + 2 * b2
	if first > second:
		return 1
	elif first == second:
		return 0
	return -1
A.sort(cmp=compare)
ans = 0
for i in xrange(n):
	ans += i * A[i][0] + (n-i-1) * A[i][1]
print ans