import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

a = []

while True:
    try:
        n= int(input())
    except:
        break
    a.append(n)

def post_order(start, end):
    if start > end:
        return
    
    mid = end + 1 # 나눌위치
    for i in range(start + 1, end + 1):
        #루트를 기준으로 잡고 나눔/ 루트보다 크면 mid에 i값을 설정하고 빠져나옴
        if a[start] < a[i]:
            mid = i
            break
           
    post_order(start + 1, mid - 1) #왼쪽 노드 
    post_order(mid, end) #오른쪽 노드
    print(a[start])

post_order(0, len(a)-1)

