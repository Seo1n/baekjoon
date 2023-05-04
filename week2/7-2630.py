import sys
input = sys.stdin.readline

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

def paper(x, y, n):
    global white
    global blue
    color = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
             if color != a[i][j]:
                paper(x, y, n//2)
                paper(x, y + n//2, n//2)
                paper(x + n//2, y, n//2)
                paper(x + n//2, y + n//2, n//2)
                return
    if color == 0:
        white += 1
    else: blue += 1

white = 0
blue = 0

paper(0,0,n)

print(white)

print(blue)



