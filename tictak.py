initial = input().split()
n = int(initial[0])
m = int(initial[1])
board = []
for i in range(0,n):
    board.append(list(input()))

print(board)

def checkCols():
    for i in range(0,n):
        
        for j in range(0,n):
            val = board[i]