t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(t):
    m, n, x, y = map(int, input().split())
    max_year = lcm(m, n)
    answer = -1  

    while x <= max_year:
        if (x - y) % n == 0:  
            answer = x
            break
        x += m 

    print(answer)
