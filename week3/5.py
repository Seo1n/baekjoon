import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = (map(int, input().split()))
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = (map(int, input().split()))
    graph[a][b] = graph[b][a] = 1

def dfs(start):
    visited[start] = True
    for i in range(1, n+1):
        if not visited[i] and graph[start][i]:
            dfs(i)

cnt = 0

dfs(1)
cnt += 1

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)


