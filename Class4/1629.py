def mod_pow(a, b, c):
    if b == 0:
        return 1

    half = mod_pow(a, b // 2, c)
    print(half, b)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (a * half * half) % c


a, b, c = map(int, input().split())

answer = mod_pow(a, b, c)

print(answer)
