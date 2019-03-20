n, m = map(int, raw_input().split())
def game23(n, m):
	if m % n != 0:
		return -1

	ret = 0
	m /= n
	while m % 2 == 0:
		m /= 2
		ret += 1
	while m % 3 == 0:
		m /= 3
		ret += 1
	if m == 1:
		return ret
	else:
		return -1
print game23(n, m)