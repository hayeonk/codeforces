A = map(int, raw_input().split())
A.sort()
ans = [str(A[-1] - x) for x in A[:3]]
print " ".join(ans)