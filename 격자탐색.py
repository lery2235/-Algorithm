import sys 
sys.stdin = open("격자탐색.txt", "rt")

#(1, n) 에서 (r, c) 내에 있는 수들 중

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
# r = 2 c = 3 # (1, 4) -> (2, 3)
for i in range(n):
    for j in range(n):
        if i >= r and j <= c - 1: 
            if board[i][j] < board[r-1][c-1]:
                board[i][j] = 0
arr.sort()
for i in range(n):
    for j in range(n):
        print(board[i][j],end =' ')
    print()