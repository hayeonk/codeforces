n, h = map(int, raw_input().split())
A = map(int, raw_input().split())

def canPut(k, h):
	nums = sorted(A[:k], reverse = True)
	if sum(nums[::2]) <= h:
		return True
	return False

lo, hi = 0, n-1
while lo < hi:
	mid = (lo + hi + 1) / 2
	if canPut(mid, h):
		lo = mid
	else:
		hi = mid - 1
if canPut(lo+1, h):
	print lo + 1
else:
	print lo