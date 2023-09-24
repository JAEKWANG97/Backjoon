# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때,
# 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


# 우선 세 합을 구하고 거기에서 가치가 큰 코인만 더했을 경우
# 큰코인으로 매꾸고 나머지가 가장 큰 코인으로 안 될 때 큰 코인보다 작은 코인으로

# 코인은 총 2개 3킬로그램과 과 5킬로그램

# 두 코인의 합은 5


# 합이 input을 넘기묜 초기화
# 한번돌때 5와 3의 갯수를 기억해야함 그래서 temp 라는 변수로 설정하겠음
# temp 라는 변수에 각 케이스의 5와 3의 조합을 넣을거

# 처음엔 5로 다 채워봄. 예를 들어 18이라고 치면 5가 3번 들어갈거
# 근데 15에서 5를 더하게 되면 18을 넘게되네?
# 그래서 20을 만드는 대신 5로 15까지 만들고 더 작은 수를 더해가는 거임
# 이게 반복되는거임
# 5로 최대한 채워보고 안되면 5보다 작은수를 하나씩 더 끼워넣는 거임

# 또다른 예로 36을 생각해보겠음
# 36은 3으로 충분히 만들 수 있음 하지만 가장 큰 수로 먼저 만들어 보겠다는 거임
# 35까지는 무난히 진행이 될거임
# 하지만 나머지 1때문에 3도 안들어갈거임
# 그래서 다시 30까지옴
# 어라 6은 3보다 작음. 3으로 다 채워 보는 거임
# 5의 max 값을 구하고 -1 씩 하면서 3한테 기회를 +a 씩 준다는거임

# 그래서 이전 5의 max값을 알고 있어야함
a = 3
b = 5
sum = 0

def grid(a: int, b: int, input: int, sum=0, current_max=None, bag=None):
    # 초깃값 세팅
    if current_max is None:
        current_max = input // b

    if bag is None:
        bag = {a: 0, b: 0}

    # 일반적으로 나올 케이스
    if sum == input:
        return bag[a] + bag[b]

    if current_max == 0:
        return -1

    if input - sum >= b and bag[b] < current_max:
        sum += b
        bag[b] += 1
        return grid(a, b, input, sum, current_max, bag)
    if input - sum >= a:
        sum += a
        bag[a] += 1
        return grid(a, b, input, sum, current_max, bag)
    # 최댓값의 max 갯수를 줄여야함
    current_max = bag[b] - 1  # 최대값의 갯수 max 초기화
    bag[a], bag[b], sum = 0, 0, 0
    return grid(a, b, input, sum, current_max, bag)


n = int(input())
print(grid(a, b, n))
