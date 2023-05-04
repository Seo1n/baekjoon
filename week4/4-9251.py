import sys
input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())

n, t = len(a), len(b)

dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        # a와 b가 일치할때, 대각선 dp값에 +1을 해준다
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else: 
# 그게 아니라면 현재 위치의 위쪽이나 왼쪽에 있는 값중 큰 값을 추가해준다
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][t])

# string_a = ' ' + sys.stdin.readline().rstrip()
# string_b = ' ' + sys.stdin.readline().rstrip()
# dp = [[0] * len(string_b) for _ in range(len(string_a))]

# for i in range(1, len(string_a)):
#     for j in range(1, len(string_b)):
#         if string_a[i] == string_b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
# print(dp[-1][-1])