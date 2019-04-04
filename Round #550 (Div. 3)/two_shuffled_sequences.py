from collections import Counter

n = input()
A = map(int, raw_input().split())
freq = Counter(A)
if max(freq.values()) > 2:
	print "NO"
else:
	inc = []
	dec = []
	for n in freq:
		inc += [n]
		if freq[n] == 2:
			dec += [n]
	inc.sort()
	dec.sort(reverse=True)
	print "YES"
	print len(inc)
	print " ".join(list(map(str, inc)))
	print len(dec)
	print " ".join(list(map(str, dec)))