import sys
input = sys.stdin.readline
from collections import deque

n= int(input())

graph= []
visited = [[-1] * (n+1) for _ in range(n+1)]

for _ in range(n):
    a = list(map(int, (input().rstrip())))
    graph.append(a)

def bfs():
     queue = deque()
     queue.append((0,0))
     dx = [-1, 1, 0, 0]
     dy = [0, 0, -1, 1]
     # visited[0][0]이 벽뚫은 횟수 카운트해줌
     visited[0][0] = 0
     while queue:
          x,y = queue.popleft()
          # 도착지점에 도달하면 카운트 횟수 반환
          if x == n-1 and y == n-1:
              return visited[x][y]
          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 흰 벽 == 빈 공간이므로 벽을 뚫지 않고도 그냥 이동할 수 있음
                # 빈 공간 위치의 우선순위를 높게 쳐서 큐의 헤드 부분에 넣어준다 == appendleft
                if graph[nx][ny] == 1:
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y] 
                 # 그렇지 않다면 빈 공간이든, 벽이든
                 # 기존의 값을 갱신할 수 있을 때만 갱신하고 위치를 큐에 담는다.
                else: 
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1



print(bfs())
