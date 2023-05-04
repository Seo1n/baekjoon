import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
#sorted는 기존 리스트 변경하지 않고 새로운 리스트 반환함. 따라서 sort써줄 것
room.sort(key=lambda x: (x[1], x[0]))
cnt = 1

end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)
