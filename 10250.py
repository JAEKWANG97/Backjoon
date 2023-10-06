t = int(input())
import sys

for _ in range(t):
    info = list(map(int, list(sys.stdin.readline().strip().split(' '))))

    h = info[0]
    w = info[1]
    n = info[2]

    if h == 1:
        floor = 1
        room = n
    else:
        floor = n % h
        if floor == 0:
            floor = h
        room = (n - 1) // h + 1

    print(f'{floor * 100 + room}')
