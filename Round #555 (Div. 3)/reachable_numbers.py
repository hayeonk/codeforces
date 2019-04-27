n = input()
cnt = set()
while n not in cnt:
	cnt.add(n)
	n += 1
	while n%10 == 0:
		n /= 10
print len(cnt)