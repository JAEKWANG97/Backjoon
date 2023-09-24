n = int(input())
x = 0
while True:
    if n % 5 == 0:
        print(n // 5 + x)
        break
    if n < 0:
        print(-1)
        break
    n -= 3
    x += 1