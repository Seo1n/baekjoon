import sys
input = sys.stdin.readline
from collections import deque

n, k = (map(int,input().split()))
dq= deque([i for i in range(1, n+1)])
l = []

for i in range(n):
    dq.rotate(-k+1) 
    a = dq.popleft()
    l.append(a)

l = str(l).replace('[', '<').replace(']', '>')
print(l)

