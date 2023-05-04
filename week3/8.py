import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())


def dfs(node):
    global result
    for i in graph[node]:
        #색 구분/ -1 = 칠해져있지 않음
        if (visited[i] == -1):
            
            #색이 1로 칠해져있는게 있다면 i = 2
            if (visited[node] == 1):
                visited[i] = 2
            #색이 2로 칠해져있는게 있다면 i = 1
            if (visited[node] == 2):
                visited[i] = 1

            dfs(i)

        else:
            # node와 지금 i의 색이 같으면 False; return
            if (visited[node] == visited[i]):
                result = False
                return

for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    visited = [-1] * (v+1)
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    result = True

    # visited는 색깔 표시해주고 dfs로 들어감
    for i in range(1, v+1):
        if (visited[i] == -1):
            visited[i] = 1
            dfs(i)
            if (result == False):
                break
    if (result == False):
        print("NO")
    else:
        print("YES")

