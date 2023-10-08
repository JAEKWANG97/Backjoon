# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

def factorial(n : int)->int:
    dp = [0] * (n+1)
    if n <= 0:
        return 1
    if n == 1:
        return 1
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] * i
    return dp[n]

n = int(input())
fact_n = factorial(n)
count = 0
while True:
    if fact_n % 10 == 0:
        count += 1
        fact_n //= 10
    else:
        break

print(count)