# 1 -> 2~7
# 2~7 -> 8~19
# 8~19 -> 20~37
# 20 ~ 37 -> 38 ~ 61


n = int(input())
root = 0
k = 0
while True:
    if n <= root:
        print(k)
        break
    root = k * (k + 1) / 2 * 6 + 1
    k += 1