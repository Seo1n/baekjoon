import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
add, subtract, multiply, divide = (map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(i, nums):
    global maximum, minimum, add, subtract, multiply, divide
    if i == n:
        maximum = max(maximum, nums)
        minimum = min(minimum, nums)
        return
    
    if add > 0:
        add -= 1
        dfs(i + 1, nums + data[i])
        add += 1
    if subtract > 0:
        subtract -= 1
        dfs(i + 1, nums - data[i])
        subtract += 1
    if multiply > 0 :
        multiply -= 1
        dfs(i + 1, nums * data[i])
        multiply += 1
    if divide > 0:
        divide -= 1
        #float 방지
        dfs(i + 1, int(nums / data[i]))
        divide += 1

dfs(1, data[0])
print(maximum)
print(minimum)


