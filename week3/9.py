import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = input().strip()

graph = [[] for _ in range(n+1)]
# place 만들어서 실내, 실외 구분해줌
place = [0] * (n+1)
visited = [0] * (n+1)


for i in range(n-1):
    u, b = map(int, input().split())
    graph[u].append(b)
    graph[b].append(u)

for i in range(len(a)):
    #input값이 1일때 place도 같이 실내 표시해주기
    if a[i] == '1':
        place[i+1] = 1

def dfs(node):
    cnt = 0
    for i in graph[node]:
        # place가 실외일 때, dfs 돌면서 실내 개수 카운트
        if place[i] == 0:
            if not visited[i]:
                visited[i] = True
                cnt += dfs(i)
        else: cnt += 1
    return cnt

total = 0

for i in range(1, n+1):
    if place[i] == 0:
        if not visited[i]:
            visited[i] = True
            # 실내개수 카운트 후 result에 dfs 값 집어넣고 n * n-1해준다
            result = dfs(i)
            total += result * (result-1)
    else: 
        #실내일때는 +1
        for j in graph[i]:
            if place[j] == 1:
                total += 1

print(total)


