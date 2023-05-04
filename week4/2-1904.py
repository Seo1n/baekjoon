import sys
input = sys.stdin.readline

n = int(input())

memo = [0] * 1000001
memo[1] = 1
memo[2] = 2

for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746

print(memo[n])

