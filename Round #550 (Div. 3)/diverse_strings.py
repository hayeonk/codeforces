def strToBin(s):
	n = 0
	for c in s:
		n += 1 << (ord(c) - ord('a'))
	return n
	
def isDiverse(s):
	n = strToBin(s)
	rightmost = n & (-n)
	n += rightmost
	return n & (n-1) == 0
		
for _ in xrange(input()):
	s = raw_input()
	if len(set(s)) != len(s):
		print "NO"
	elif isDiverse(s):
		print "YES"
	else:
		print "NO"