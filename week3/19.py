import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

coins = (set(int(input()) for _ in range(n)))

visited = [0 for _ in range(k+1)]
queue = deque()

# 코인이 구하려는 값보다 크지 않은 경우에만 append해준다
# 근데 이거 밑에 코드랑 겹침 불팔요하긴한데 수정하기귀찮음
for coin in coins:
    if not coin > k:
        queue.append([coin, 1])
        visited[coin] = 1

while queue:
    value, num_coin = queue.popleft()
    if value == k:
        print(num_coin)
        break

    for coin in coins:
        if value + coin > k:
            continue
        if visited[value + coin] == 0:
            visited[value + coin] = 1
            queue.append((value + coin, num_coin+1))
            
else: print(-1)




