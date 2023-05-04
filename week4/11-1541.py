import sys
input = sys.stdin.readline

# - 기준으로 split하게되면 숫자가 분할됨; 그걸 기준으로 n[1:]는 다 마이너스 처리가능
n = input().split('-')
cnt = 0

# 플러스밖에 없다면 다 더해주게끔 설정되어있음
for i in n[0].split('+'):
    cnt += int(i)
for i in n[1:]:
    for j in i.split('+'):
        cnt -= int(j)

print(cnt)