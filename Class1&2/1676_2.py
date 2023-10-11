# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 10으로 나눠지는 
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


def custom_factorial(n:int)->int:
    dp = [0] * (n+1)
    if n <= 0:
        return 1
    if n == 1:
        return 1
    dp[0] = 0
    dp[1] = 1
    two = 0
    fiv = 0
    for i in range(2,n+1):
        temp = i
        while True:
            if i % 2 == 0:
                i //= 2
                two += 1
            elif i % 5 == 0:
                i //= 5
                fiv += 1
            else:
                break
        dp[i] = dp[i-1] * i
    return dp[n] , two , fiv

print(custom_factorial(500))