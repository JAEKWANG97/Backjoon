import sys

str = list(sys.stdin.readline().strip().split(' '))

n = int(str[0])
m = int(str[1])

pocketmon_arr = []

for _ in range(n):
    pocketmon_arr.append(sys.stdin.readline().strip())

pocketmon_dict = dict()

for index , pocketmon in enumerate(pocketmon_arr):
    pocketmon_dict[pocketmon] = index


for _ in range(m):
    cmd = sys.stdin.readline().strip()
    try :
        print(pocketmon_arr[int(cmd)-1])
    except ValueError:
        print(pocketmon_dict[cmd]+1)

        