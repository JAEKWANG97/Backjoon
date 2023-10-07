import sys
arr = list(map(int , list(sys.stdin.readline().strip().split(' '))))



if arr == sorted(arr):
    print('ascending')
elif arr == sorted(arr, reverse=True):
    print('descending')
else:
    print('mixed')