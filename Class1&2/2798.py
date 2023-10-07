str = input().split(" ")
str = list(map(int, str))
n = str[0]
m = str[1]
card = input().split(" ")
card = list(map(int, card))

card.sort()
combi = dict()
# 두개의 합의 조합 부터 만든다.
for i in range(len(card)):
    for j in range(i + 1, len(card)):
        if card[i] + card[j] < m and m - (card[i] + card[j]) >= card[0]:
            combi[m - (card[i] + card[j])] = [card[i], card[j]]


# 나머지 한개를 찾는다.

sum = list(combi.keys())
sum.sort()
# print(sum)
value = 0
for x in sum:
    # print(combi[x])
    temp = [y for y in card if y <= x if (y not in combi[x])]
    temp.sort()
    if temp:
        if value < temp[-1] + combi[x][0] + combi[x][1]:
            value = temp[-1] + combi[x][0] + combi[x][1]

print(value)
