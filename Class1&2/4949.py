import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    stack = []
    for x in string:
        if x in ('(', '['):
            stack.append(x)
        elif x == ')':
            if not stack or stack.pop() != '(':
                stack.append(x)
                break
        elif x == ']':
            if not stack or stack.pop() != '[':
                stack.append(x)
                break
                    
    print('yes' if not stack else 'no')
