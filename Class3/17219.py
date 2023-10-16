# 딕셔너리 활용문제임
# n = 주소, 비밀번호 리스트 수, m은 찾으려는 주소 비밀번호 수

# 출력 => 비밀번호

import sys

n , m = map(int,sys.stdin.readline().strip().split())

password_dict = {}

for _ in range(n):
    adress , password = sys.stdin.readline().strip().split(' ')
    if adress not in password_dict:
        password_dict[adress] = password
        
for _ in range(m):
    adress = sys.stdin.readline().strip()
    print(password_dict[adress])