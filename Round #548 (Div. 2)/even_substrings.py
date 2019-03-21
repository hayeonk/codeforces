n = input()
s = map(int, list(raw_input()))
cnt = 0
for i in xrange(n):
	if s[i]%2 == 0:
		cnt += i + 1
print cnt