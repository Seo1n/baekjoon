a= input().split()
A= a[0]
B= a[1]
if A[::-1] > B[::-1]:
    print(A[::-1])
else: print(B[::-1])