from collections import deque
import sys
input = sys.stdin.readline

n= int(input())
dq= deque([i for i in range(1, n+1)])

while len(dq) > 1:
    dq.popleft()
    ans = dq.popleft()
    dq.append(ans)

print(dq[0])    

# dq.rotate(-1) 왜안됨 ..?


