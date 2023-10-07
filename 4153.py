# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 
# 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
import sys

while True:
    str = list(map(int,list(sys.stdin.readline().strip().split())))
    str.sort()
    if sum(str) == 0:
        break
    if str[0]**2 + str[1]**2 == str[2]**2:
        print('right')
    else:
        print('wrong')
    
