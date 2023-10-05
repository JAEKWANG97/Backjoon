# 1 부터 n 까지 오름차순으로 주어진 수열이 있다.
# 주어진 수열을 만드려면 스택에 1~n 을 push/pop 을 사용해서 만들어야 한다.

# n 은 수열의 길이
# 그 다음부터는 수열

# 예를 들어 n이 8이고 수열 [4,3,6,8,7,5,2,1] 이 주어진다고 가정하자.

# 스택에서는 4를 만들기 위해 push를 4번 한 후 pop. 스택은 [1,2,3]
# 3을 만들기 위해 pop. 스택은 [1,2,]
# 6을 만들기 위해 스택에 push push==> [1,2,5,6] , pop [1,2,5]
# 8을 만들기 위해 push push pop [1,2,5,7]
# 7 -> pop
# 5-> pop
# 2 -> pop
# 1 -> pop

import sys

n = int(sys.stdin.readline())

sequence = [i for i in range(1,n+1)]
stack = []
answer = []
current = 1

for _ in sequence:
    num =int(sys.stdin.readline())
    while current <= num:
        stack.append(current)
        answer.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop() 
        answer.append('-')
    else:
        print('NO')
        break
else:
    for op in answer:
        print(op) 
