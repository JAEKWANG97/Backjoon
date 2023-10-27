
n, r, c = map(int, input().split())

def search_value(n,c,r):
    if n == 0 :
        return 0
    
    half = 2**(n-1)
    quadrant = find_quadrant(n,c,r)
    
    if quadrant == 1:
        return search_value(n-1,c,r)
    if quadrant == 2:
        return half*half + search_value(n-1,c- half,r )
    if quadrant == 3: 
        return 2 * half * half +search_value(n-1,c ,r- half) 
    if quadrant == 4:
        return 3 * half * half + search_value(n-1,c - half,r - half)

def find_quadrant(n,c,r):
    if r < 2**(n-1):
        if c < 2**(n-1):
            return 1
        else:
            return 2
    else:
        if c < 2**(n-1):
            return 3
        else:
            return 4

        
print(search_value(n,c,r))