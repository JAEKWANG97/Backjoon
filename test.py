arr = [0, 1, 2]

for i in range(3):
    new_arr = arr[:i] + arr[i+1:]  # i번째 인덱스를 제외한 새로운 리스트 생성
    print(new_arr)
