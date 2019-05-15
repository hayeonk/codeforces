n = input()
A = map(int, raw_input().split())
cnt = 0
for n in sorted(A):
	if n < cnt + 1:
		continue
	else:
		cnt += 1
print cnt