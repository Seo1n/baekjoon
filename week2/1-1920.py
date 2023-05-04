import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for i in b:
    left = 0
    right = n - 1
    l = False

    while left <= right:
        mid = (left + right) // 2
        if i == a[mid]:
            l = True
            print(1)
            break
        elif i> a[mid]:
            left = mid + 1
        else: right = mid - 1
    
    if l == False:
        print(0) 
   


