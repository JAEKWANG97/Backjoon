import sys
str = sys.stdin.readline().rstrip().split(' ')
n = int(str[0])
k = int(str[1]) - 1
arr = []
temp = k
for i in range(1, n+1):
    arr.append(int(i))

new_arr = []
while arr:
    new_arr.append(arr.pop(k))
    k = k + temp
    while(arr):
        if(k >= len(arr)):
            k = k % len(arr)
        else:
            break


print("<" , end="")
for i in new_arr:
    if(i == new_arr[-1]):
        print(i , end="")
        break
    print(i , end=", ")

print(">" , end="")
