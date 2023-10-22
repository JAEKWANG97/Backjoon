# 자연수의 제곱근을 최대 4개 사용해서 수를 만들어야함
# 제일 가까운 제곱수를 이용해야ㅑ함 
# 나머지를 이용한 DP
def dp_table(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4,n+1):
        temp = int(i ** 0.5)
        dp[i] = dp[i-temp**2] + 1
        for j in range(temp):
            temp -= 1
            dp[i] = min(dp[i] , dp[i-temp**2]+1)

    return dp[n]
n = int(input())
print(dp_table(n))