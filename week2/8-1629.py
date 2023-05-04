import sys
input = sys.stdin.readline

a,b,c = list(map(int, input().split()))

def num(a,b,c):
    if b == 1:
        return (a % c)
        
    elif b % 2 == 0:
        return (num(a, b//2, c) ** 2) %c
    else: 
        return((num(a, b//2, c) ** 2)*a) %c

print(num(a,b,c))  

# https://hooongs.tistory.com/108

