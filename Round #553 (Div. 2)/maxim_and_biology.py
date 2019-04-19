n = input()
s = raw_input().strip()
def getDistance(s):
	g = "ACTG"
	ans = 0
	for i in xrange(4):
		dist = abs(d[s[i]] - d[g[i]])
		if 26 - dist < dist:
			dist = 26 - dist
		ans += dist
	return ans

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = {}
for c, num in zip(a, range(26)):
	d[c] = num
ans = 4 * 26
for i in xrange(4, n+1):
	ans = min(ans, getDistance(s[i-4:i]))
print ans