from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
q= PriorityQueue()

for i in range(n):
    a = int(input())
    if a == 0:
        if q.qsize() == 0:
            print(0)
        else: print(q.get()[1])
    else: q.put((-a, a))
