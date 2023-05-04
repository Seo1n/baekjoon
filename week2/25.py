import sys
import heapq
input = sys.stdin.readline

n = int(input())
l_heap = [] # 가장 위에 있는 값이 중간값이 되어야하므로 최대 힙 사용
r_heap = [] # 최소 힙 
ans = []

for i in range(n):
    num = int(input())
    if len(l_heap) == len(r_heap): # 길이가 같을 때 left heap에 먼저 값 넣어줌
        heapq.heappush(l_heap, (-num, num))
    else:
        heapq.heappush(r_heap, (num, num))
    
    # left heap에 있는 값이 더 클때 서로 값을 바꿔서 넣어줌
    if r_heap and l_heap[0][1] > r_heap[0][0]:
        a = heapq.heappop(l_heap)[1]
        b = heapq.heappop(r_heap)[0]
        heapq.heappush(l_heap, (-b, b))
        heapq.heappush(r_heap, (a, a))
    ans.append(l_heap[0][1]) #맨 위에 있는 값은 ans list에 append

for i in ans:
    print(i)
    