import sys

str = list(map(int,list(sys.stdin.readline().strip().split())))

n = str[0]
k = str[1]

# 파스칼 삼각형 만들기 
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1
# ... (계속됨)

#n번째 k ==> 이항 계수

rows, cols = n, k 
dp = [[0] * (i+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
    if i > 0 :
        dp[i][i] = 1

for i in range(2,n+1):
    for j in range(1,i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])
print(dp[n][k])