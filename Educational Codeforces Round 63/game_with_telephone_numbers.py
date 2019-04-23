n = input()
s = raw_input().strip()
turn = (n-11)/2
erase = 0
cnt = 0
for i in xrange(n):
	if s[i] == "8":
		cnt += 1
	elif erase == turn:
		break
	else:
		erase += 1
if cnt > turn:
	print "YES"
else:
	print "NO"