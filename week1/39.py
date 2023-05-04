import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n= int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
ans = []

def dfs(x, y, k):
    if x < -1 or y < -1 or x >= n or y >= n:
        return False
    
    if graph[x][y] > k and visited[x][y] == False:
        visited[x][y] = True

        dfs(x+1, y, k)
        dfs(x-1, y, k)
        dfs(x, y+1, k)
        dfs(x, y-1, k)

        return True
    return False

for k in range(101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i,j,k):
                cnt += 1

    ans.append(cnt)
    if cnt == 0:
         break
    
print(max(ans))

