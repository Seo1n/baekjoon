import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for i in range(n):
    a = int(input())
    if a <= k:
        coins.append(a)

coins.sort(reverse=True)
cnt = 0

for coin in coins:
   cnt += (k// coin)
   k %= coin

print(cnt)

