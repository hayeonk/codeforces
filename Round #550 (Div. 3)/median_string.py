n = input()
s = raw_input()
t = raw_input()
d = {}
S = "abcdefghijklmnopqrstuvwxyz"
for c, num in zip(list(S), range(26)):
	d[c] = num
	
def getMedian(s, t, n):
	ans = ""
	num = d[s[-1]] + d[t[-1]]
	
	for c1, c2 in reversed(zip(s[:-1], t[:-1])):
		num += (d[c1] + d[c2]) * 26
		ans += S[(num/2) % 26]
		num /= 26
	ans += S[(num/2) % 26]
	return "".join(reversed(ans))

print getMedian(s, t, n)