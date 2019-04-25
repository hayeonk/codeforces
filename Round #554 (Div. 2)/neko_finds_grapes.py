n, m = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
print min(len([x for x in A if x%2]), len([x for x in B if x%2==0])) + min(len([x for x in A if x%2==0]), len([x for x in B if x%2]))