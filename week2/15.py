import sys
input = sys.stdin.readline

n = int(input())
dq = [int(input()) for _ in range(n)]
cnt = 1
max_h = dq[-1]

for i in range(n):
    end = dq.pop()
    if max_h < end:
        cnt += 1
        max_h = end

print(cnt)
    
    
        
