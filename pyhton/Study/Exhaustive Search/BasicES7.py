import sys 
sys.stdin = open("BasicES7.txt", "rt")

r, c = map(int, input().split())
board = [list(map(str, input().split()))for _ in range(r)]

for i in board:
    print(i)
count = 0

for i in range(r):
    for j in range(c - 1):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                    if board[0][0] != board[i][j] and \
                    board[i][j] != board[k][l] and \
                    board[k][l] != board[r - 1][c - 1]:
                         count += 1

print(count)