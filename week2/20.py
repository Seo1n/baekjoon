from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    a = input().strip()
    if a == 'pop':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
            queue.popleft()
    elif a.split()[0] == 'push':
        queue.append(a.split()[1])
    elif a == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif a == 'size':
        print(len(queue))
    elif a == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif a == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
