from collections import Counter
from fractions import gcd

n = input()
A = map(int, raw_input().split())
B = map(int, raw_input().split())
freq = Counter([(b/gcd(a,b), a/gcd(a,b)) for a, b in zip(A, B) if a])
rest = sum(a==b==0 for a, b in zip(A, B))
print max(freq.values()) + rest if freq else rest