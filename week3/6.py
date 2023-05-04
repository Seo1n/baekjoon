import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
cnt = -1
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    global cnt
    queue= deque([v])
    visited[v] = True
    while queue:
        p = queue.popleft()
        cnt += 1
        for i in range(n+1):
            if not visited[i] and graph[p][i]:
                queue.append(i)
                visited[i]= True

bfs(1)
if cnt < 0:
    print(0)
print(cnt)