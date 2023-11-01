import sys

n = int(input())

arr = [list(map(int, input().split()))for _ in range(n)]

def slice_arr(n,arr,num)-> arr:
    new_arr = []
    if num == 1:
        for i in range(n//2):
            new_arr.append(arr[i][0:n//2])
        return new_arr
    if num == 2:
        for i in range(n//2):
            new_arr.append(arr[i][(n//2):n])
        return new_arr
    if num ==3:
        for i in range(n//2 , n):
           new_arr.append(arr[i][0:n//2])
        return new_arr
    if num == 4:
        for i in range(n//2,n):
            new_arr.append(arr[i][n//2:n])
        return new_arr

def search_blue(n,arr) -> int:
    if n == 1:
        return arr[0][0], 1 - arr[0][0]
    
    blue_count, white_count = 0, 0
    if sum(map(sum, arr)) == n * n:
        blue_count = 1
    elif sum(map(sum, arr)) == 0:
        white_count = 1
    else:
        for i in range(1, 5):
            blue, white = search_blue(n//2, slice_arr(n, arr, i))
            blue_count += blue
            white_count += white

    return blue_count, white_count

blue_count , whtie_count = search_blue(n,arr)
print(whtie_count)
print(blue_count)