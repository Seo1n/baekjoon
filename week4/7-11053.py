import sys
input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))

dp = [1] * (n+1)

# 포문을 이렇게 돌리게 되면 i = 2일때, j는 0과 1이다.
# 그래서 계속 이전 숫자들과 현재 숫자를 비교할 수 있다
for i in range(1, n):
    for j in range(i):
        if seq[j] < seq[i]:
            # 현재값과 이전값 +1 중 큰 값을 넣는다
            dp[i] = max(dp[i], dp[j] + 1)

# 그중 가장 큰 수를 출력한다
print(max(dp))

