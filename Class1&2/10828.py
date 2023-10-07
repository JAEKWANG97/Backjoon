import sys

n = int(sys.stdin.readline().rstrip())
arr = []


while(n>0):
    cmd = sys.stdin.readline().rstrip().split(' ')
    match cmd[0]:
        case 'push':
            arr.append(cmd[1])
        case 'pop':
            if(arr):
                temp = arr[-1]
                del arr[-1]
                print(f"{temp}")
            else:
                print(-1)
        case 'top':
            if(arr):
                temp = arr[-1]
                print(f"{temp}")
            else:
                 print(-1)
        case 'empty':
            if(arr):
                print(0)
            else:
                print(1)
        case 'size':
            print(f"{len(arr)}")
    n -= 1