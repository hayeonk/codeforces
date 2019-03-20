from collections import Counter

n, k = map(int, raw_input().split())
nums = map(int, raw_input().split())
nums = [x % k for x in nums]
mdict = Counter(nums)
cnt = 0
for x in mdict:
	if x == 0 or x == k - x:
		cnt += (mdict[x] / 2) * 2
	else:
		cnt += min(mdict[x], mdict[k-x])
print cnt