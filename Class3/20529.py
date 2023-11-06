from collections import defaultdict

def cal_gap(mbti1, mbti2, mbti3):
    gap = 0
    for i in range(4):
        if mbti1[i] != mbti2[i]:
            gap += 1
        if mbti1[i] != mbti3[i]:
            gap += 1
        if mbti2[i] != mbti3[i]:
            gap += 1
    return gap

# 입력 받는 부분
T = int(input().strip())

# 각 테스트 케이스마다
for _ in range(T):
    n = int(input().strip())  # 학생 수
    mbtis = input().strip().split()  # 학생들의 MBTI 유형
    mbti_dict = defaultdict(int)
    
    # MBTI 유형 카운트
    for mbti in mbtis:
        mbti_dict[mbti] += 1

    # 조기 종료 조건 확인
    if n > 32 or any(count >= 3 for count in mbti_dict.values()):
        print(0)
        continue

    ans = float("inf")

    # 가능한 모든 3개의 MBTI 조합에 대해 최소 거리 계산
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                ans = min(ans, cal_gap(mbtis[i], mbtis[j], mbtis[k]))

    print(ans)
