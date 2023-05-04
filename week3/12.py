import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heavy_list = [[] for _ in range(n+1)]
light_list = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    heavy_list[a].append(b)
    light_list[b].append(a)

def dfs(list, ball):
    cnt = 0
    for i in list[ball]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            cnt += dfs(list, i)
    return cnt

mid = (n+1) // 2
ans = 0

for i in range(1, n+1):
    visited = [0] * (n+1)
    if dfs(heavy_list, i) >= mid:
        ans += 1
    if dfs(light_list, i) >= mid:
        ans += 1

print(ans)