import sys
from collections import deque
T = int(sys.stdin.readline().strip())

for _ in range(T):
    cmd = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip()[1:-1]

    if nums:
        nums = deque(map(int, nums.split(',')))

    order_index = True
    error = False
    for c in cmd:
        if c == "R":
            order_index = not order_index
        elif c == "D":
            if nums:
                if order_index:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                print("error")
                error = True
                break

    if not error:
        if not order_index:
            nums.reverse()  
        nums = ','.join(map(str, nums)) 
        print("[" + nums + "]")
