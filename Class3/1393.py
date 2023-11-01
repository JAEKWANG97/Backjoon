t = int(input())
import sys
meeting_list = []
for i in range(t):
    start ,end = map(int, sys.stdin.readline().strip().split())
    meeting_list.append([start,end])
    

meeting_list.sort(key=lambda x : (x[1],x[0]))
count = 1
i = 1
j = 0
while i < t and j < t:
    end_time = meeting_list[j][1]
    start_time = meeting_list[i][0]
    if end_time <= start_time:
        count += 1
        j = i
    i += 1

print(count)