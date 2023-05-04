import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                queue.append([i, j])
            elif graph[i][j] == 'S':
                queue.appendleft([i,j])
            elif graph[i][j] == 'D':
                a,b = i, j

def bfs():
    check = False
    while queue:
        if check == True:
            break
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <r and 0<= ny <c:
                if graph[x][y] == '*':
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
                        graph[nx][ny] = '*'
                        queue.append([nx,ny])

                elif graph[x][y] == 'S':
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = 'S'
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx,ny])
                    elif graph[nx][ny] == 'D':
                        check = True
                        visited[nx][ny] = visited[x][y] + 1
                        break

bfs()

if visited[a][b] == 0:
    print('KAKTUS')
else: print(visited[a][b])

        


