n = input()
l = raw_input()
r = raw_input()
ldict = {}
rdict = {}
key = "abcdefghijklmnopqrstuvwxyz?"
for c in key:
	ldict[c] = []
	rdict[c] = []
	
for i, c in enumerate(l):
	ldict[c].append(i+1)
	
for i, c in enumerate(r):
	rdict[c].append(i+1)
	
cnt = 0
pair = []
lleft = []
rleft = []
for i in xrange(len(key)-1):
	left = ldict[key[i]]
	right = rdict[key[i]]
	for _ in xrange(min(len(left), len(right))):
		cnt += 1
		pair.append([left.pop(), right.pop()])
	lleft += left
	rleft += right
	
ql = ldict[key[-1]]
qr = rdict[key[-1]]
while ql:
	if rleft:
		pair.append([ql.pop(), rleft.pop()])
	elif qr:
		pair.append([ql.pop(), qr.pop()])
	else:
		break
	cnt += 1
	
while qr:
	if lleft:
		pair.append([lleft.pop(), qr.pop()])
	elif ql:
		pair.append([ql.pop(), qr.pop()])
	else:
		break
	cnt += 1
	
print cnt
for i, j in pair:
	print i, j