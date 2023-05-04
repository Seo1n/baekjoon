import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    m = int(input())
    lst = [list(map(int, input().split())) for _ in range(m)]
    lst.sort()
    ans = []
    
    test = lst[0][1]
    cnt = 1
    for j in range(1, m):
        if lst[j][1] < test:
            test = lst[j][1]
            cnt += 1

    print(cnt)

