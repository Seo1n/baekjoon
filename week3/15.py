import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

INF = int(1e9)
table = [INF] * (n+1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    # 순서는 꼭 우선순위, 값 형태로
    heapq.heappush(q, (0, start))
    # 시작노드(ex. 1)에서 1로 가는 거리는 없으므로 0
    table[start] = 0

    while q:
        # 탐색할 거리와 노드를 가져옴
        dist, node = heapq.heappop(q)

        # 기존 거리보다 길다면 체크하지 않음
        if table[node] < dist:
            continue

        for i in graph[node]:
            # cost = 인접노드까지의 거리 탐색
            cost = table[node] + i[1]
            # cost가 기존 거리보다 짧다면 테이블을 갱신한다
            if cost < table[i[0]]:
                table[i[0]] = cost
                # 다음으로 인접한 거리를 계산하기 위해 큐에 삽입
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(table[end])

