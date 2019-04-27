n = input()
a = map(int, list(raw_input().strip()))
d = map(int, raw_input().split())
check = False
for i in xrange(n):
	if d[a[i]-1] > a[i]:
		a[i] = d[a[i]-1]
		check = True
	elif d[a[i]-1] == a[i]:
		continue
	elif check:
		break
print "".join(map(str, a))