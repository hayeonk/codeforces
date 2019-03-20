H, n = map(int, raw_input().split())
damage = map(int, raw_input().split())

def kill(H, damage, n):
	damage_sum = sum(damage)
	damage_max = cur = 0
	for i in xrange(n):
		cur += damage[i]
		damage_max = min(damage_max, cur)
	
	if H + damage_max > 0 and damage_sum >= 0:
		return -1
	
	ret = 0
	if damage_sum == 0:
		for i in xrange(n):
			if H <= 0:
				return ret
			H += damage[i]
			ret += 1
		
	ret = max(0, (H + damage_max) / -damage_sum)
	if H + damage_max > 0 and (H + damage_max) % -damage_sum != 0:
		ret += 1
	H += damage_sum * ret
	ret *= n
	
	for i in xrange(n):
		if H <= 0:
			break
		H += damage[i]
		ret += 1
	
	return ret
	
print kill(H, damage, n)