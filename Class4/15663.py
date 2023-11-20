from itertools import permutations

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
permutation = list(permutations(arr, m))

for x in permutation:
    print(*x)
