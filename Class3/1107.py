n = str(input())
m = int(input())
if m != 0:
    excepted_nums = list(map(int , (input().strip().split())))
    available_nums = [(i) for i in range(10) if not i in excepted_nums]
else:
    excepted_nums = []
    available_nums = [(i) for i in range(10) if not i in excepted_nums]

available_nums = set(available_nums)
channel = 100
value = -1
n_list = list(map(int,list(n)))
min_gap = 10000000
for x in range(1000000):
    if set(list(map(int,list(str(x))))) <= available_nums:
        gap = abs(x-int(n))
        if gap < min_gap:
            min_gap = gap
            value = x
if value >= 0:
    print(min(abs(int(n)-value) + len(list(str(value))) , abs(channel - int(n))))
else:
    print(abs(channel - int(n)))