import sys
input = sys.stdin.readline
from collections import deque

# (1,2)와 같은 그래프 문제가 나올 때 구해야하는 것을 변수로 만들어주기
# ex) place, distance
# graph[p]에서 탐색
n, m, k, x = map(int, input().split())

graph= [[] for _ in range(n + 1)]
visited = [0] * (n+1)
distance = [0] * (n+1)

for i in range(m):
    a,b = list(map(int, input().split()))
    # 단방향 그래프
    graph[a].append(b)

def bfs(start):
    ans = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                # 지금까지의 거리 + 1 해서 distance[i]에 저장
                distance[i] = distance[p] + 1
                if distance[i] == k:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i)

bfs(x)

