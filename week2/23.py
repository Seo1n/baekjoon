from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break

print(cnt)

# n= int(input())
# board = [[0] * n for _ in range(n)]

# k = int(input())
# for _ in range(k):
#     x, y = (map(int,input().split()))
#     board[x - 1][y - 1] = 1 #0,0에서 시작하기 때문에 -1해줌

# L = int(input())
# dx = [-1, 0, 1, 0] #(1,0) 남 (-1,0) 북
# dy = [0, 1, 0, -1] #(0,1) 동 (0,-1) 서


# time = {}
# for i in range(L):
#     l,d = input().split()
#     time[int(l)] = d

# direction = 1
# cnt = 0
# nx, ny = 0,0
# snakes = deque([(0, 0)])

# def change(d):
#     # 상(0) 우(1) 하(2) 좌(3)
#     # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
#     # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
#     if d == "L":
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return d

# while True:
#     cnt +=1 
#     nx += dx[direction]
#     ny += dy[direction]

#     if cnt in time.keys():
#         change(time[cnt])

#     if nx< 0 or nx >= n or ny < 0 or ny >= n:
#         break

#     if board[nx][ny] == 1:
#         board[nx][ny] = 0
#         snakes.append([nx,ny])
    
#     elif board[nx][ny] == 0:
#         snakes.append([nx,ny])
#         a,b = snakes.popleft()

# print(cnt)













