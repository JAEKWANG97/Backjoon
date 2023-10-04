# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
# n(문서의 개수) , m(궁금한 문서가 Queue에 몇 번째로 놓여 있는지를 나타내는 정수) = 1, 0
# m이 몇 번째로 출력되었는지가 궁금한거임

# 순서는 0번 부터 시작임. 두번째줄에는 N개 문서의 중요도가 차례대로 주어져있음 

# 4 2
# 1 2 3 4

# 문서의 개수는 4, 궁금한 문서는 2, queue에는 1,2,3,4 가 중요도. 0부터니까 1,2,3,4에서는 중요도 3을 궁금해 하는거임 따라서 중요도 순으로 재배열하고 하면 4 다음에 3. 그러므로 답은 2
# 중요도 순으로 정렬해서 인덱스를 찾으면 되긴 하는데 
# 중복되는 중요도가 있는 경우는 먼저 앞에 위치한 인덱스 먼저 출력하게 된다.
# 예를 들어 6
# 6 0
#  9 2 1 1 1 1 
# 이라는 케이스가 있다고 가정하면, 맨 앞의 중요도 1을 가진 문서의 출력 순서를 알아내야한다.
# 하지만 중복되는 중요도가 있다.
# 우선 큐에서는 9를 먼저 내보낼 것이다. 
# 나머지는 1 을 출력하는데, 이때 맨 앞에 있던 1을 출력하는게 아니라 9뒤에 있는 1부터 출력한다.
# 위치에 따른 우선순위에서 중요도 기준 맨 뒤로 보내지는것.


import sys
import time
T = sys.stdin.readline()

arr=[]
for _ in range(int(T)):
    nm = sys.stdin.readline().split(' ')    
    n = int(nm[0])
    m = int(nm[1])
    que = list(sys.stdin.readline().rstrip().split(' '))
    que = list(map(int, que))

    que_dict = dict()
    for value, key in enumerate(que):
        que_dict[value] = key

    que.sort(reverse=True)
    arr=[0] * n
    for index, (key, value) in enumerate(que_dict.items()):
        arr[index]= [key, value]

    i = 0
    while i < n or que:
        if que[0] > int(arr[i][1]):
            arr.append(arr.pop(i))
        else:
            que.pop(0)
            i+=1

    for i in range(n):
        if arr[i][0] == m:
            print(i+1)

# 1 2 3 4 

# 2 3 4 1

# 3 4 1 2

# 4 1 2 3

# 4 2 3 1

# 4 3 1 2

# 4 3 2 1


    

    # print(que.index(doc) + 1)

