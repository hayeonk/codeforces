n = input()
A = map(int, raw_input().split())
ones = ans = 0
for i in xrange(n):
	while A[i] >= 2 and ones:
		ans += 1
		ones -= 1
		A[i] -= 2
	ans += A[i]/3
	ones += A[i]%3
	
print ans