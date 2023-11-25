from itertools import combinations

coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]

result = 5
n = len(cards)
select_cards = cards[:n // 3]
round = 0
select_card = list(combinations(select_cards , 2))
for cards in select_card:
    if n+1 == sum(cards):
        select_cards.remove(cards[0])
        select_cards.remove(cards[1])
        round += 1

for cards