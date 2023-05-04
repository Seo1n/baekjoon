a= input()
b= int(a)

if b % 4 == 0 and b % 100 != 0 or b % 400 == 0:
    print(1)
else: print(0)