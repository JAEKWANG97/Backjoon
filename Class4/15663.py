from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
permutation = list(combinations_with_replacement((arr), m))

for x in sorted(set(permutation)):
    print(*x)
