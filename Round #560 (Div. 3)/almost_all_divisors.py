for _ in xrange(input()):
	n = input()
	A = set(map(int, raw_input().split()))
	d = min(A) * max(A)
	
	s = set()
	for i in xrange(2, int(d**0.5) + 1):
		if d % i == 0:
			s.add(i)
			s.add(d / i)
	
	if set(A) != s:
		print -1
	else:
		print d