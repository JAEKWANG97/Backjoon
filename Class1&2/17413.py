import sys

str = list(sys.stdin.readline().rstrip())
arr = []
i = 0
tmp = []

while(i < len(str)):
    if(str[i] == '<'):
        tmp.append(i)
    if(str[i] == '>'):
        tmp.append(i)
    i+=1
j=0
value = ""
while(1):
    if(j+3 < len(tmp)):
        print(''.join(str[tmp[j]: tmp[j+1]+1]) , end='')
        temp = str[tmp[j+1]+1 : tmp[j+2]]
        print(''.join(temp[::-1]),end='')
        j+=2
    else:
        print(''.join(str[::-1]),end='')
        break


