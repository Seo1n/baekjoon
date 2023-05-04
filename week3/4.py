import sys
input = sys.stdin.readline
from collections import deque

n, m, v = (map(int, input().split()))

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  # a,b가 1,4라고 가정하면 graph 1 4/ 4 1만 true표시해줌
  # 간선이 양방향이라 둘다 표시해줘야함/ 연결되어있으면 True
  graph[a][b] = graph[b][a] = True 

def bfs(start, visited):
    queue = deque([start])
    #시작지점만 True로 바꿔주고 queue에 넣어줌
    visited[start] = True

    while queue:
        p = queue.popleft()
        print(p, end= ' ')
        for i in range(1, n+1):
# graph[p][i] == [시작지점][i] 여기서 아까 True 표시한 a,b와 같을 경우 i를 append해줌
            if not visited[i] and graph[p][i] == True:
                queue.append(i)
                # visited가 모두 True가되면 탐색 종료
                visited[i] = True

def dfs(start, visited):
    visited[start] = True
    print(start, end= ' ')
    for i in range(1, n + 1):
        if not visited[i] and graph[start][i]:
            #재귀 돌면서 visited[i]는 모두 True표시됨
            # return값 없어도 알아서 종료
            dfs(i, visited)

dfs(v, visited2)
print()
bfs(v, visited1)





