# 계단 오르기 문제임
# 근데 조건이 있음
# 1 or 2 계단 씩 가능
# 마지막 계단은 꼭 밟아야함
# 근데 3연속 계단은 안댐 --> 1 1 1 => x

import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

# 연속된 계단 밝는걸 어케 막음?
# 이전 3 계단 까지 확인해야함
# dp  = max( i-1 i-2) 에서 i-1이 이전 dp[i-4] + arrp i-3 arr i-2 arri-1 이면 i-2를 선택하도록
# 근데 이 방법은 그냥 조건만 걸어두는거지 max를 찾는게 아닌 것 같음
# 2차원 배열을 이용해서 연속계단의 수를 적어두는 거임
def dp_table(n : int , arr : []) -> int:
# 그래서 생각해낸 방법이 1계단 + 2계단 해서 올라오는 방법과 2계단 + 1계단 올라서 도달하는 방법임
    dp = [0] * (n+1)
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[1] + arr[0]
    dp[1] = arr[0]
    dp[2] = arr[1] + arr[0]
    if n <= 2:
        return dp[n]
    for i in range(3,n+1):
        dp[i] = max((dp[i-3]+arr[i-2]+arr[i-1]) , dp[i-2]+arr[i-1])
        
    return dp[n]


print(dp_table(n,arr))