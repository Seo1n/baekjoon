a= int(input())

for i in range(0, a):
    b,c= input().split()
    d= int(b)
    result= str()
    for i in c:
        result += i*d
    print(result)


    
