n, maxb, maxa = map(int, raw_input().split())
A = map(int, raw_input().split())
ans = 0
b, a = maxb, maxa
for n in A:
	if a == b == 0:
		break
	if n == 0:
		if a > 0: a -= 1
		else: b -= 1
	else:
		if b > 0:
			if a == maxa: a -= 1
			else:
				b -= 1
				a += 1
		else:
			a -= 1
		
	ans += 1
	
print ans