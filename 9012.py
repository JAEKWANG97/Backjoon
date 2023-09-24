import sys

n = int(input())
arr = []

for i in range(0, n):
    result = ""
    stk_num = int(0)
    arr = sys.stdin.readline()
    arr = list(arr)
    arr.pop()
    for j in range(0, len(arr)):
        match arr[-1]:
            case "(":
                stk_num -= 1
                arr.pop()
            case ")":
                stk_num += 1
                arr.pop()
        if stk_num < 0:
            result = "NO"
            break
    if stk_num != 0:
        result = "NO"
    else:
        result = "YES"

    print(result)
