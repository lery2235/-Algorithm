import sys 
from collections import deque

sys.stdin = open("토마토.txt", "rt")

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
queue = deque()
dis = [[0] * n for _ in range(m)]
dx, dy = [1, 0, -1, 0],[0, -1, 0, 1]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            queue.append((i,j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1 
            queue.append((nx,ny))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
res = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
           if dis[i][j] > res:
               res = dis[i][j]
    print(res)
else:
    print(-1)