l, r = map(int, raw_input().split())
mod = 1000000007

def cnt(n):
	take = 1
	idx = 0
	cnt = [0, 0]
	
	while take < n:
		cnt[idx] += take
		n -= take
		take *= 2
		idx = 1 - idx
	
	cnt[idx] += n
	return cnt

def getSum(n):
	o, e = cnt(n)
	return o * o + e * (e + 1)
	
ans = (getSum(r) - getSum(l-1)) % mod
print ans