# 영화감독 지겹다

# 666 => 9로 치환

# 1 -> 19
# 2 -> 29
# 3 -> 39

#포인터를 써서 9가 어디에 들어가야 가장 이상적인가......
#1~10000 까지
# 4 -> 49
# 5 -> 59
# 6 -> 69
# 7 -> 79

'''
1 666
2 1666
3 2666
4 3666
5 4666
6 5666
7 6666
8 7666
9 8666
10 9666
11 10666
'''

# 아 몰라 브루트포스로 해

def find_flim_name(n):
    n = n-1
    count=0
    arr = [0] * (n+1)
    i =0
    while True:
        count+=1
        if '666' in str(count):
            arr[i] = count
            i+=1
        if i > n: break
    return arr[n]

print(find_flim_name(500))