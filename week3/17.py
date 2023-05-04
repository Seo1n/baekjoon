import sys
input = sys.stdin.readline
from collections import deque

#3차원배열 ~!!
m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

ans = 0
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        x,y,z = queue.popleft()
        
        #값이 1인 지점을 가지고 BFS수행 > 6개의 이동 수 고려하기
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 값이 0인 지점을 이전값에 1을 더해서 업데이트하기 
            if 0<= nx < h and 0 <= ny < n and 0 <= nz < m:
                if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz))
                    box[nx][ny][nz] = box[x][y][z] + 1
                    visited[nx][ny][nz] = 1

for a in range(h):
    for b in range(n):
        for c in range(m):
            # 값이 1인 지점을 모두 queue에 append한다
            if box[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a,b,c))
                visited[a][b][c] = 1

bfs()

# bfs 탐색 후에도 0이 나온다면 -1 반환
for a in box:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        # 최대값 반환
        ans = max(ans, max(b))

print(ans-1)