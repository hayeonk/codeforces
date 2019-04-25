from fractions import gcd
a, b = map(int, raw_input().split())
def factors(n):
	ret = []
	for i in xrange(1, int(n**0.5) + 1):
		if n % i == 0:
			ret.append(i)
			if n / i != i:
				ret.append(n / i)
	return ret
	
if a > b:
	a, b = b, a
	
minVal = (a * b) / gcd(a, b)
ans = 0
for n in factors(b-a):
	i = n - (a % (n))
	val = (a+i) * (b+i) / gcd(a+i, b+i)
	if val < minVal:
		minVal = val
		ans = i
print ans