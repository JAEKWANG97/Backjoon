from collections import deque
import collections

def isPalindrome(s : str)-> bool:
    strs: deque = collections.deque()
    for char in s:
        strs.append(char)
    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False
    return True
            

import sys

n = int(sys.stdin.readline().strip())
input_str = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())

def dp_table(input_str ,n ):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # 길이가 1인 부분 문자열
    for i in range(n):
        dp[i][i] = 1
        
    # 길이가 2인 부분 문자열
    for i in range(n-1):
        if input_str[i] == input_str[i+1]:
            dp[i][i+1] = 1
            
    # 길이가 3 이상인 부분 문자열
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if input_str[i] == input_str[j] and dp[i+1][j-1]:
                dp[i][j] = 1
    return dp



dp = dp_table(input_str , n)
for _ in range(m):
    s, e = map(int, sys.stdin.readline().strip().split())
    print(dp[s-1][e-1])