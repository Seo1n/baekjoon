import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
result= [0] * n

stack = []

for i in range(n):
    while stack:
        #스택에 추가된 값과 현재 값을 비교 => 현재값보다 스택 값이 작다면 수신 불가/ pop해줌
        if a[i] > stack[-1][1]:
            stack.pop()
        else : 
            # 스택 값이 크다면 수신가능/ +1해서 위치를 저장해줌
            result[i] = stack[-1][0] + 1
            break
    # 스택에 아무것도 없으면 append
    stack.append((i, a[i]))
    
for i in range(n):
    print(result[i])
