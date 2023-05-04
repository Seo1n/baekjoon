import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
ans = 0

for i in range(n):
    a= int(input())
    heapq.heappush(heap, a)

if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            ans += n1 + n2
            heapq.heappush(heap, (n1 + n2))
                  
    print(ans)





