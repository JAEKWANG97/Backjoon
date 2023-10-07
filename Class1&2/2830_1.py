a = 3
b = 5
sum = 0
# 더하기 말고 곱하기로 ㄱㄱ
bag = {3: 0, 5: 0}
n = int(input())
current_max = n // 5
value = None

while sum != n:
    if (n - sum) >= b and bag[5] < current_max:
        sum += b
        bag[5] += 1
        continue
    if (n - sum) >= a:
        sum += a
        bag[3] += 1
        continue
    else:
        #  근데 5의 맥스값을 다 죽였는데도 불구하고 n 값이 안만들어진다. 이거는 -1을 내놔야함
        if current_max == 0:
            value = -1
            break
        current_max = bag[5] - 1  # 최대값의 갯수 max 초기화
        bag[3], bag[5], sum = 0, 0, 0  # 가방 초기화 , sum 초기화

if value != -1:
    value = bag[5] + bag[3]

print(value)
