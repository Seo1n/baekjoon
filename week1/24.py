N= int(input())
a= list(map(int, input().split()))

result = 0
for i in a:
    num = 0
    for n in range(2, i+1):
        if i % n == 0:
            num += 1
    if num == 1:
        result += 1
print(result)












        
