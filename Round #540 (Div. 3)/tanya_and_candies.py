n = input()
nums = map(int, raw_input().split())
odd = sum(nums[2::2])
even = sum(nums[1::2])
cnt = 1 if odd == even else 0

for i in xrange(1, n):
	if i%2 == 0:
		odd += nums[i-1] - nums[i]
	else:
		even += nums[i-1] - nums[i]
	if odd == even:
		cnt += 1
		
print cnt