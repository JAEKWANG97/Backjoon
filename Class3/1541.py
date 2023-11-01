import re

expression = input().strip()

# 숫자와 연산자(+,-)로 분리
tokens = re.split('([+-])', expression)
numbers = [int(num) for num in tokens[::2]]
operators = tokens[1::2]


sum = 0

flag = True
# - 를 최대한 묶어야함
for x in tokens:
    if x =='-':
        flag = False
    if x.isdigit():
        if flag:
            sum += int(x)
        else:
            sum -= int(x)
print(sum)