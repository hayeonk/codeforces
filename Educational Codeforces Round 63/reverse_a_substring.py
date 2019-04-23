n = input()
s = raw_input().strip()
ans = []
for i in xrange(n-1):
	if s[i] > s[i+1]:
		ans += [i+1, i+2]
		break
if ans:
	print "YES"
	print " ".join(map(str, ans))
else:
	print "NO"