import sys
input = sys.stdin.readline

n, k = map(int, input().split())

backpack= [[0,0]]
for _ in range(n):
    backpack.append(list(map(int, input().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

# 무게 = 1일때 넣을 수 있는 값을 표에 삽입해줌
# 그래서 k값에 도달했을 때 넣을 수 있는 최적의 값을 찾아주는거임
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = backpack[i][0]
        value = backpack[i][1]
        # 넣으려는 물건의 무게가 더 클 때
        if j < weight:
            # 옆의 값 가져옴
            dp[i][j] = dp[i-1][j]
        else: # 가방에 넣을 수 있다면
            # 아까 값이 더 큰지, 새로운 값이 더 큰지 판별해서 넣어줌
            # ex) 6kg = 13의 값이 최적/ dp[i-1][6 - 6]+ 13 = 13 삽입
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])

