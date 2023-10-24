# 패션왕이 되어 보자!

"""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""

import sys  

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    closet = dict()
    for _ in range(n):
        cloth,category = sys.stdin.readline().strip().split(' ')
        if category not in closet:
            closet[category] = 0
        closet[category]+=1
    
   
    combination = 1
    count = 0
    category = 0
    for key , value in closet.items():
        combination *= value + 1
        
    print(combination - 1)