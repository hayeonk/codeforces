k = input()
v = ["a", "e", "i", "o", "u"]
n = m = None
for i in xrange(5, int(k**0.5) + 1):
	if k % i == 0:
		n = i
		m = k / i
		break
if not n:
	print -1
else:
	ans = []
	row = v * (n/5) + v[:n%5]
	for i in xrange(m):
		ans.extend(row[i:] + row[:i])
	print "".join(ans)