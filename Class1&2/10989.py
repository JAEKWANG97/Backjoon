# 힙 정렬?

# 기수 정렬

# 기수란 숫자의 자릿수다. 예를 들면 42는 4와 2의 두개의 자릿수를 가지고 이것이 기수가 된다.
# 기수 정렬이란 이러한 자릿수의 값에 따라서 정렬하기 때문에 기수 정렬이라는 이름을 얻었다. 

# 기수 정렬은 다단계 정렬인데, 단계의 수는 데이터의 전체 자릿수와 일치한다. 

# n자릿수까지 있는 리스트를 정렬하는 방법은 
# 0부터 n까지 번호가 매겨진 n개의 버킷을 준비한다.
# 그리고 난 후, n의 자리수부터 정렬을 하는데, 

# 만약 3405 라는 수 그리고 리스트의 최고 자릿수는 1000 이라고 가정하면,
# 3405는 준비해둔 1의 자릿수부터 인덱스 5인 배열에 들어가게 된다.
# 그리고 0인 인덱스, 그리고 4, 그리고 3 으로 하면 최종적으로 1000의 자리 배열에는 
# 인덱스 3 에 3405가 저장된다. 

#  n ---> [1의 자리 버킷] --> [10의 자리 버킷] --> [100의 자리 버킷] --> [1000의 자리 버킷]

import sys

n = int(sys.stdin.readline().strip())

def make_buckets():
    return [[] for _ in range(10)]
    
max_len = 0
arr = []
for _ in range(n):
    num = sys.stdin.readline().strip()
    if max_len < len(num): max_len = len(num)
    arr.append(int(num))


for i in range(max_len-1  , -1 , -1): # 최대 자릿수 만큼 버킷을 업데이트해야함
    buckets = make_buckets()
    # 1의 자리 버켓부터 만듬
    for num in arr: # 버킷에 든 인덱스별 배열들을 순회하면서 다음 버킷에 넘겨야함
        x = str(num).zfill(max_len) # 해당값에 최대자릿수만큼 0을 만듬
        buckets[int(x[i])].append(num) # 다음 버켓의 인덱스 배열에 해당 자릿수 확인하여넘김
    arr = []
    for bucket in buckets:
        for x in bucket:
            arr.append(x)
        

for num in arr:
    print(num)

