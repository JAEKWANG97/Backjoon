# 피보나치 수열을 만들어라

def make_fibo(n : int):
    if n <=0:
        return 0
    if n ==1 :
        return 1
    
    dp = [0] * (n+1)
    dp[1] =1
    dp[2] =1 
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def nth_fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    yield a

# 사용 예제
value = next(nth_fibonacci(10))
print(value)  # 34
# print(make_fibo(int(input())))