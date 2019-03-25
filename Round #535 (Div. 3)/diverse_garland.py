n = input()
S = list(raw_input())
ret = 0
for i in xrange(1, n):
	if S[i] == S[i-1]:
		l = ["R", "G", "B"]
		l.remove(S[i])
		if i < n-1 and S[i+1] in l:
			l.remove(S[i+1])
		S[i] = l[0]
		ret += 1
print ret
print "".join(S)