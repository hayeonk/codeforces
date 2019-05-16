import sys
from fractions import gcd

A = []
Q = []
print "? 1 2"
sys.stdout.flush()
Q.append(input())
print "? 2 3"
sys.stdout.flush()
Q.append(input())
print "? 3 4"
sys.stdout.flush()
Q.append(input())
print "? 4 5"
sys.stdout.flush()
Q.append(input())

N = [4 , 8, 15, 16, 23, 42]
d = {}
for i in xrange(6):
	for j in xrange(i+1, 6):
		d[N[i] * N[j]] = set([N[i], N[j]])
last = 7418880
nums = [set(), set(), set(), set()]
for i in xrange(4):
	nums[i] = d[Q[i]]
			
ans = [list(nums[i] & nums[i+1])[0] for i in xrange(3)]
ans.insert(0, Q[0] / ans[0])
ans.append(Q[-1] / ans[-1])

for n in ans:
	last /= n
ans.append(last)

print "! " + " ".join(map(str, ans))