friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
from collections import defaultdict


def solution(friends, gifts):
    memo = defaultdict(int)
    gift_index = defaultdict(int)
    next_gift = defaultdict(int)
    for gift in gifts:
        giver, getter = gift.split(' ')
        gift_index[giver] += 1
        gift_index[getter] -= 1
        memo[gift] += 1
    max_gift = 0
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            key = friends[i] + " " + friends[j]
            rev_key = friends[j] + " " + friends[i]
            if memo[key] > memo[rev_key]:
                next_gift[friends[i]] += 1
            elif memo[key] < memo[rev_key]:
                next_gift[friends[j]] += 1
            else:
                if gift_index[friends[i]] > gift_index[friends[j]]:
                    next_gift[friends[i]] += 1
                elif gift_index[friends[i]] < gift_index[friends[j]]:
                    next_gift[friends[j]] += 1
        max_gift = max(max_gift , next_gift[friends[i]] , next_gift[friends[j]])
    answer = max_gift
    return answer


sol = solution(friends, gifts)
print(sol)
