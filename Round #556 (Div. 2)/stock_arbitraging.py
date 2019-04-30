n, m, r = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
if min(A) >= max(B):
	print r
else:
	cnt = r / min(A)
	r %= min(A)
	r += max(B) * cnt
	print r