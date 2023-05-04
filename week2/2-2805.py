import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

h = list(map(int, input().split()))
h.sort()

left, right = 1, h[-1]

while left <= right:
    h = 0
    mid = (left + right) // 2
     
    for i in h:
        if i >= mid:
            h += i-mid
    
    if h >= m:
        left = mid + 1

    else: right = mid -1

print(right)  

