import sys
rl = lambda: sys.stdin.readline().split()

for _ in xrange(input()):
	n = input()
	s = raw_input().strip()
	if n < 11:
		print "NO"
	else:
		if "8" in s[:n-10]:
			print "YES"
		else:
			print "NO"