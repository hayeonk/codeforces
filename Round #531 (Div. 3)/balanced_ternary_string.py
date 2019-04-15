n = input()
s = raw_input().strip()
num = [s.count(c) - n / 3 for c in "012"]

for x in [0, 2, 1]:
	if num[x] < 0:
		for y in xrange(3):
			if num[y] > 0:
				cnt = min(-num[x], num[y])
				num[x] += cnt
				num[y] -= cnt
				if x > y:
					s = s[::-1].replace(str(y), str(x), cnt)[::-1]
				else:
					s = s.replace(str(y), str(x), cnt)
print s