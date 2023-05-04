def n_queen(x):
    if x == N:
        global count
        count += 1
        return
    
    for y in range(N):
        board[x] = y

        if check(x):
            n_queen(x+1)
     
def check(x):
     for y in range(x):
            if board[x] == board[y] or (x-y == abs(board[x]- board[y])):
               return False
     return True

N= int(input())
count = 0
board = [0 for _ in range(N)]

n_queen(0)

print(count)



