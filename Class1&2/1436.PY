


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

print(find_flim_name(int(input())))