from collections import Counter
from collections import defaultdict
n, k = map(int, raw_input().split())
A = map(int, raw_input().split())
F = Counter(A)
if F.most_common(1)[0][1] > k or n < k:
	print "NO"
else:
	d = defaultdict(list)
	cur = 1
	for n in sorted(A):
		d[n].append(cur)
		cur = cur + 1 if cur < k else 1
	ans = [str(d[n].pop()) for n in A]
	print "YES"
	print " ".join(ans)