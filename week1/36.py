import sys
input = sys.stdin.readline

n_list = []

for i in range(0, 9):
    n = int(input())
    n_list.append(n)

for i in range(9):
    for j in range(i+1, 9):    
        if sum(n_list) - n_list[i] - n_list[j] == 100:
            ln = n_list[i]
            jn = n_list[j]
            break

n_list.remove(ln)
n_list.remove(jn)

n_list.sort()
ans = [print(i) for i in n_list]





