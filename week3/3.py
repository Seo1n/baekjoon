#작은쪽을 테이블에 넣게됨
# ex) 1과 2가 연결되었을 때 2번째 자리에 1이 들어가게끔 만드는것임
# 그리고 3이라는 다른 수가 들어왔을 때 2와 연결되면 3이 가르키고 있는 2를 찾음 
# >> 결국 3번째 자리에도 1이 들어가게됨. 그래서 재귀가 사용됨

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(E)]

c.sort(key= lambda x: x[2])

#작은 노드를 저장해줄 테이블/ 처음에 모든 값은 자기 자신을 가리킴
table = [i for i in range(V+1)]
ans = 0

# find로 테이블[x] == x 같을 때까지 찾아줌
def find(x):
    if x != table[x]:
        return find(table[x])
    return table[x]

def unit(a,b):
    a= find(a)
    b = find(b)
    if a > b:
        table[a] = b
    else: 
        table[b] = a

for a, b, cost in c:
    if find(a) != find(b):
        unit(a,b)
        ans += cost

print(ans)


