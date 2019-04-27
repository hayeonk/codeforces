import sys
n, k = map(int, raw_input().split())

def search(i, j):
	hi = i * (2 ** k - 1)
	lo = k * i + (k-1)*k/2
	if lo <= n <= hi:
		return i
	while i <= j:
		mid = (i + j) / 2
		hi = mid * (2 ** k - 1)
		lo = k * mid + (k-1)*k/2
		if lo <= n <= hi:
			return mid
		elif hi < n:
			i = mid + 1
		else:
			j = mid - 1
	return -1
		
ans = []
s = search(1, n)
if s == -1:
	print "NO"
	sys.exit()

ans = [s]
k -= 1
n -= s
while k:
	s = search(s+1, s*2)
	ans.append(s)
	n -= s
	k -= 1
print "YES"
print " ".join(map(str, ans))