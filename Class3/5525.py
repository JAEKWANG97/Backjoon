n = int(input())
m = int(input())
s= input()



i=0
count = 0
while i < m:
    if s[i] == "I":
        cnt = 0
        while i + 2 < m and s[i + 1] == 'O' and s[i + 2] == 'I':
            i+= 2
            cnt += 1
            if cnt >= n:
                count +=1
        
    i+=1

print(count)