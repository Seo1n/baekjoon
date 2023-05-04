#공유기 설치

import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))

x = [int(input()) for _ in range(n)]
x.sort()

start = 1

end = x[-1] - x[0] 

ans = 0

while start <= end: # 최솟값 == 최댓값일 때 while문 종료
    mid = (start + end) // 2
    m = min(x)
    cnt = 1  # 거리를 mid로 두었을 때 가능한 집 개수 카운트

    for i in range(1, len(x)):
        if x[i] >= m + mid: # x의 값이 최솟값 + 중간값보다 클 때
            cnt += 1
            m= x[i]  
    
    if cnt >= c: # 집의 개수가 공유기의 갯수보다 크거나 같게 측정됐을 때 
        start = mid + 1 # 더 작은 수가 있을 수 있으니 더 탐색 진행
        ans = mid # ans에 mid 값 저장/ ans는 최대 거리 == 최대 중간 값
    else: end = mid - 1

print(ans)




