from collections import Counter

n = input()
nums = map(int, raw_input().split())
freq = Counter(nums)
q = []
b = []
o = []
for k in freq:
	while freq[k] >= 4:
		q.append(k)
		freq[k] -= 4
	if freq[k] >= 2:
		b.append(k)
		freq[k] -= 2
	if freq[k]:
		o.append(k)
		
if n % 2 == 0:
	if b or o:
		print "NO"
	else:
		ret = [[] for _ in xrange(n/2)]
		for i in xrange(n/2):
			for j in xrange(n/2):
				k = q.pop() 
				ret[i].append(str(k))
		for i in xrange(n/2):
			ret[i] += reversed(ret[i])
		for i in reversed(xrange(n/2)):
			ret.append(ret[i])
		
		print "YES"
		for row in ret:
			print " ".join(row)
else:
	while q and len(b) < n - 1:
		x = q.pop()
		b.append(x)
		b.append(x)
	if len(o) != 1 or len(b) != n-1:
		print "NO"
	else:
		ret = [[] for _ in xrange(n/2+1)]
		for i in xrange(n/2+1):
			for j in xrange(n/2+1):
				if i == j == n/2:
					ret[i].append(str(o.pop()))
				elif i == n/2 or j == n/2:
					ret[i].append(str(b.pop()))
				else:
					ret[i].append(str(q.pop()))
							
		for i in xrange(n/2+1):
			ret[i] += reversed(ret[i][:-1])
		for i in reversed(xrange(n/2)):
			ret.append(ret[i])
		
		print "YES"
		for row in ret:
			print " ".join(row)