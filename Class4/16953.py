a, b = map(int, input().split())
count = 0

while b > a:
    # B가 홀수이고 마지막 숫자가 1이 아니면 A를 B로 만들 수 없음
    if b % 2 == 1 and b % 10 != 1:
        break
    if b % 2 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    count += 1

print(count + 1 if a == b else -1)
