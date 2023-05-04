import sys
input = sys.stdin.readline
from collections import deque

n = int(input())


for i in range(n):
    dq= deque(input().strip()) 
    count = 0
    for j in dq:
            if j == '(':
                count += 1
            elif j == ')':
                count -= 1
            if count < 0:
                print('NO')
                break
    if count == 0:
        print('YES')
    elif count > 0:
         print('NO')    



# n = int(input())   
# stack = []
# seq = []

# for i in range(n):
#     a= input().strip()
#     seq.append(a)
#     for j in seq:
#         if j == ')' and len(stack) == 0:
#             print('NO')
#             break
#         elif j == '(':
#             stack.append(j)
#         elif j == ')':
#             stack.pop()
#     if len(stack) > 0:
#         print('NO')
#     else: print('YES')