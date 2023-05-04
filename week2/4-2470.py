import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))
a.sort()

start = 0
end = n-1

result = abs(a[start] + a[end]) #맨 왼쪽 + 오른쪽 절대값
ans = [a[start], a[end]] 

while start < end:
    left = a[start]
    right = a[end]

    sum = left + right # 왼쪽, 오른쪽 포인터
  
    if abs(sum) < result: # 포인터의 절대값이 지금 결과값보다 작다면 결과값 업데이트
        result = abs(sum)
        ans = [left, right]
        if result == 0:
          break
    if sum < 0: # sum이 음수라면 왼쪽으로, 양수라면 오른쪽으로 (0과 가깝게 만들기)
        start += 1
    else:
        end -= 1

print(ans[0], ans[1])