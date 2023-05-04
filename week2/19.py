import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
num = list(input().strip())

stack = []
cnt = k

for i in range(n):
    while stack and cnt > 0:
        if stack[len(stack) -1] < num[i]:
            stack.pop()
            cnt -= 1
        else: break
    stack.append(num[i])

print(''.join(stack[:n-k])) 