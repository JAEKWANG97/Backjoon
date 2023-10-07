n = int(input())


for i in range(0,n):
    str = input()

    arr = str.split(' ')

    result = ""
    for i in range(0,len(arr)):
        result += arr[i][::-1]
        result += " "

    print(result)

