import sys

num = sys.stdin.readline().strip().split(' ')
n = int(list(num)[0])
m = int(list(num)[1])
check_board = []

area = m * n + 1

for _ in range(int(n)):
    check_board.append(list(sys.stdin.readline().strip())) 


# 체스판 다시 칠하기
def make_checkboard(n : int , m : int , start_char : chr) -> list:
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        if i == 0 :
            arr[0][0] = start_char
        elif arr[i-1][0] == 'W':
            arr[i][0] = 'B'
        else:
            arr[i][0] ='W'
        for j in range(1,m):
            if arr[i][j-1] == 'W':
                arr[i][j] = 'B'
            else:
                arr[i][j] = 'W'
    return arr

def compare_checkboard(arr : [] , check_board : [] , n:int , m:int):
    count = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] != check_board[n+i][m+j]:
                count += 1
    return count

count = float('inf')
w_check = make_checkboard(n,m,'W')
b_check = make_checkboard(n,m,'B')
for i in range(n-7):
    for j in range(m-7):
        count = min(count , compare_checkboard(w_check , check_board , i , j) ,compare_checkboard(b_check , check_board , i , j) )

print(count)

