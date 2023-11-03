from collections import defaultdict
from itertools import combinations

# 입력 받는 부분
T = int(input().strip())  # 테스트 케이스의 수

# MBTI 유형 생성
mbti_types = [a+b+c+d for a in "EI" for b in "SN" for c in "TF" for d in "JP"]

# 각 테스트 케이스마다
for _ in range(T):
    n = int(input().strip())  # 학생 수
    mbtis = input().strip().split()  # 학생들의 MBTI 유형
    min_distance_sum = float('inf')  # 가능한 최대 거리로 초기화
    
    # 3명의 학생 조합을 모두 탐색
    for combo in combinations(mbtis, 3):
        # 현재 조합의 심리적 거리 합계 계산
        distance_sum = sum(sum(a != b for a, b in zip(combo[i], combo[j])) for i in range(3) for j in range(i+1, 3))
        
        # 최소 거리 합계 갱신
        min_distance_sum = min(min_distance_sum, distance_sum)
    
    # 가장 가까운 세 학생 사이의 심리적 거리 출력
    print(min_distance_sum)
