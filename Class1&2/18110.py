# 절사평균이란 극단적인 값들이 평균을 왜곡하는 것을 막기 위해 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것을 말한다. 30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다. 따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는 평균 계산에 반영하지 않는다는 것이다.

# 제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.

# 마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.

import sys

n = int(sys.stdin.readline().strip())
arr = []
def custom_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

for i in range(n):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
cut_num = custom_round(n*0.15)
arr.sort()
# 절삭 평균을 위해 배열을 잘라야하는데
# 위에서 15프로 아래서 15프로이다.
# 하지만 배열의 길이가 절삭 평균을 위해 잘라내는 길이와 같다면,
# 배열은 빈 배열이 되므로 안된다. 하지만 이는 애초에 잘라내는 값이 
# 원 배열의 30프로이기 때문에 그럴 일은 없다.

# 봐야할 것은. 입력값들의 합이 0인지 확인해야하는 것이다.

#반례가 있다. 

# 찾아보니 ROUND 함수는 0.5 초과인 경우 반올림을한다.
# 문제에서 제안하는 방식은 0.5 이상인 경우를 반올림 하는 것이다. 

# 때문에 커스텀 ROUND 함수를 만듬


if sum(arr) > 0 and len(arr) > 2:
    arr = arr[cut_num : - cut_num]
    print(custom_round(sum(arr) / len(arr)))
elif len(arr) == 1:
    print(arr.pop())
else:
    print(0)