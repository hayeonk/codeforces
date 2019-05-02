from collections import Counter
from itertools import permutations

def isNei(c1, c2):
	if ord(c1) + 1 == ord(c2) or ord(c1) - 1 == ord(c2):
		return True
	return False
	
def make(picked, pickFrom):
	global ret
	if not ret:
		if not pickFrom:
			ret += picked
			return
		for i in xrange(len(pickFrom)):
			if not picked or not isNei(picked[-1], pickFrom[i]):
				make(picked + [pickFrom[i]], pickFrom[:i] + pickFrom[i+1:])
	
for _ in xrange(input()):
	s = raw_input().strip()
	C = Counter(s)
	S = list(set(s))
	ret = []
	make([], S)
	
	if not ret:
		print "No answer"
	else:
		ans = ""
		for c in ret:
			ans += c * C[c]
		print ans