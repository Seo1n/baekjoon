import sys
import heapq
input = sys.stdin.readline

n = int(input())
rail = [list(map(int, input().split())) for _ in range(n)]
d = int(input())

lst = []

#(35, 25) << (25,35)로 정렬
for i in rail:
    if i[0] > i[1]:
        i[0], i[1] = i[1], i[0]

# 주어진 선로의 길이보다 작거나 같으면 리스트에 추가함
    if i[1] - i[0] <= d:
        lst.append(i)

#2번째값 기준으로 오름차순 정렬
lst.sort(key = lambda x: x[1])

heap = []
cnt = 0

for i in lst:
    if not heap:
        heapq.heappush(heap, i)
    else: # heap의 첫번째 값이 2번째값 - 선로 길이보다 작다면 pop
        while len(heap) != 0 and heap[0][0] < i[1] - d:
            heapq.heappop(heap)
        heapq.heappush(heap, i)
        #가지고 있는 max 값 프린트
    cnt = max(cnt, len(heap))

print(cnt)