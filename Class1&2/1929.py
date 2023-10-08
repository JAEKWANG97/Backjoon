# 에라토스테네스의체

# 1~n 까지의 수가 있다.
# 2를 남기고 나머지 제거
# 3을 남기고 나머지 제거 
# ....
# ....
# 소수 완성!

n , m = (input().split(' '))

print(n, m)

arr = [x for x in range(1,int(m)+1)]

print(arr)

decimal = []

for i in range(2, len(arr)):
    decimal.appen(i)
    for i in range(len(arr)):
        # decimal 의 배수 인덱스를 다 제거 할거임
    if i in arr:
        print(i)
    