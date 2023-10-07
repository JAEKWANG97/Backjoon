import sys 

# 배열안에 수를 찾아내는 법
n = int(sys.stdin.readline().strip())
a_arr= sorted(map(int, list(sys.stdin.readline().strip().split(' '))))
m = int(sys.stdin.readline().strip())
m_arr= list(map(int, list(sys.stdin.readline().strip().split(' '))))

def binary_search(target : int , arr : list) -> bool:

    low , high = 0 , len(arr)-1
    while low <= high:
        mid = (low+high) // 2 
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return True
        
    return False

for i in range(m):
    if binary_search(m_arr[i] , a_arr):
       print(1)
    else:
       print(0)