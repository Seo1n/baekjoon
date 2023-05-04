x, y= (map(int, input().split()))
n= int(input())

width = [0, x]
height= [0, y]

for _ in range(n):
    a,b = map(int, input().split())
    if a == 0:
        height.append(b)
    elif a == 1: 
        width.append(b)

width.sort()
height.sort()

result = 0

for i in range(1, len(width)):
    for j in range(1, len(height)):
        w = width[i] - width[i-1]
        h=  height[j] - height[j-1]
        result = max(result, w*h)

print(result)













