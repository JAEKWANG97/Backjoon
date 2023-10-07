import sys



while True:
    n = sys.stdin.readline().strip()
    if int(n) == 0:
        break
    left = 0
    right = len(n) - 1
    value = 'yes'
    while left <= right:
        if n[left] != n[right]:
            value = 'no'
        left    += 1
        right   -= 1

    print(value)