input= input('').split()

x= int(input[0])
y= int(input[1])
w= int(input[2])
h= int(input[3])

print(min(x,y,w-x,h-y))




