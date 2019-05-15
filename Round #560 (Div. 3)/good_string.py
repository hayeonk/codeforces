n = input()
s = raw_input().strip()
ans = []
last = s[0]
for i in xrange(1, n):
	if last != s[i]:
		ans += [last, s[i]]
		if i + 1 < n:
			last = s[i+1]
		else:
			break
print n - len(ans)
print "".join(ans)