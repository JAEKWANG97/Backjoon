t = int(input())

for _ in range(0,t):
    n = int(input())
    n = bin(n)
    n = str(n)
    i = 0
    for x in reversed(n):
        if x == "1":
            print(i , end=" ")
        i+=1