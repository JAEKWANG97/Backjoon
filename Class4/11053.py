def lis(arr):
    n = len(arr)
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1

    return max(lis_lengths)


n = int(input())
arr = list(map(int, input().split()))
result = lis(arr)
print(result)  