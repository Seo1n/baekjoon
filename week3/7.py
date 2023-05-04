import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
#DFS는 항상 부모에서 자식으로 이동함
# 문제에서 트리의 루트를 1이라고 정했기 때문에 1부터 DFS 탐색을 시작하고, 1과 연결되어 있는 Node들 중에 방문하지 않은 노드를 방문하는데,
# 이 때 visited배열의 index에 탐색을 시작한 node(즉, 부모 노드) 를 저장한다. 
# 이렇게 되면 visited에 0이 아닌 수가 저장이 되기 때문에 다시 방문하지 않는다.

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#visited = False면 visited 배열에 부모 노드를 저장
# 그러면 visited는 0이 아니게 되기 때문에 다시 방문하지 않음
def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

# for i in range(2, n + 1):
#     print(visited[i])

print(graph)