import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, (input().split()))

graph= []

for _ in range(n):
    a = list(map(int, (input().rstrip())))
    graph.append(a)

def bfs(x,y):
    #상하좌우 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        
        # 상하좌우 다 체크하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 위치를 벗어나면 안되므로 조건이 추가됨 n,m = 그래프 끝과 0 = 그래프 시작점
            # 현재 좌표값이 1이면 벽이 없으므로 이동 가능
            if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # queue에 현재좌표 추가
                queue.append((nx, ny))
                # 그 전 값에 +1을 해서 이동할 때 지나야하는 최소 칸 수를 더해준다
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


print(bfs(0,0))


# [1,0,1,1,1,1]					[3, 0, 9, 10, 11, 12]
# [1,0,1,0,1,0]					[2, 0, 8,  0, 12,  0]
# [1,0,1,0,1,1]					[3, 0, 7,  0, 13, 14]
# [1,1,1,0,1,1]					[4, 5, 6,  0, 14, 15]