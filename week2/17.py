import sys
input = sys.stdin.readline

n = int(input())
l = []

for i in range(n):
    x,r = list(map(int,input().split()))
    l.append((x-r, '(')) #왼쪽 좌표
    l.append((x+r, ')')) #오른쪽 좌표

# 좌표기준 오름차순이지만 같은 좌표값이면 ')'가 먼저옴 -아스키코드값   
l = sorted(l, key= lambda x:(x[0], -ord(x[1])))

stack= []
ans = 1

for i in range(n*2):
    position, bracket = l[i]
    if len(stack) == 0:
        stack.append({'pos': position, 'bracket': bracket, 'status': 0})
        continue

    if bracket == ')':
        #마지막 status값 확인 후 0이면 +1, 1이면 +2
        if stack[-1]['status'] == 0:
            ans += 1
        elif stack[-1]['status'] == 1:
            ans += 2
        stack.pop() # 오른쪽 괄호는 무조건 pop해서 빼줌

        if i != n*2-1: #마지막 ')' 값이 아닐 때
            if l[i+1][0] != position: # 다음 원과 좌표가 같지않으면 status = 0 변경
                stack[-1]['status'] = 0 
    else: 
        if stack[-1]['pos'] == position: #좌표값이 같으면 원이 겹쳐있음
            stack[-1]['status'] = 1
            # 다음 스택
            stack.append({'pos': position, 'bracket': bracket, 'status': 0})
        else:
            stack.append({'pos': position, 'bracket': bracket, 'status': 0})
print(ans)


                

