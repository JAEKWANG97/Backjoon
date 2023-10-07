import sys

n = int(sys.stdin.readline().strip())
word_dict = dict()
max_word = 0 
for i in range(n):
    word = sys.stdin.readline().strip()
    if len(word) not in word_dict:
        word_dict[len(word)] = []
    if len(word) > max_word:
        max_word = len(word)
    word_dict[len(word)].append(word)

for i in range(max_word+1):
    if i in word_dict:
        [print(x) for x in sorted(set(word_dict[i]))]