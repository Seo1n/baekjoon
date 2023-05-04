import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
n_list = []
count = 0
visited = [False] * N

def num(n):
    if len(n_list) == N:
        global count
        maximum = 0
        for i in range(N-1):
            maximum += abs(n_list[i] - n_list[i+1])
        count = max(count, maximum)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            n_list.append(A[i])
            num(n+1)
            n_list.pop()
            visited[i] = False

num(0)
print(count)


            
