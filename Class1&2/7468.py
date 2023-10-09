import sys

n = int(sys.stdin.readline().strip())
arr = []
wh = []
for i in range(n):
    nums = list(map(int,list(sys.stdin.readline().strip().split(' '))))
    w = nums[0]
    h = nums[1]
    arr.append((w,h))
    

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank+=1
    print(rank)
    

# 몸무게와 키가 큰 사람이 덩치가 크다.
# 몸무게와 같은 경우 키로 비교
# 키가 같은 경우 몸무게로 비교
# 몸무게가 크지만 키가 작은 경우 는 같은 등수
# 키가 크지만 몸무게가 적은 경우 는 같은 등수


