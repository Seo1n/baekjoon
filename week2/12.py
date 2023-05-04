import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    a = input().strip()

    if a == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()
    elif a.split()[0] == 'push':
        stack.append(a.split()[1])
    elif a == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif a == 'size':
        print(len(stack))
    elif a == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
