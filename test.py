from collections import defaultdict
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort(reverse=True)
    
    num_dict = defaultdict(int)
    for i in range(n):
        num_dict[arr[i]] += 1
    arr_set = list(set(arr))
    arr_set.sort(reverse=True)
    ans = 0
    for x in (arr):
        if num_dict[x] > 0 :
            ans += x
            num_dict[x] -= 1
            if arr_set.index(x) + 1 < len(arr_set):
                num_dict[arr_set[arr_set.index(x) + 1]] -= 1

                
    print(ans)
    
