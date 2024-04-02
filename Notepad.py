import sys 
sys.stdin = open("Notepad.txt", "rt")
from collections import deque
'''
# 2차원 배열을 구현합니다.
arr = [
    [0 for _ in range(10)]
    for _ in range(10)
]
for i in arr:
	print(i)

max_val = -1

# n, m을 입력받습니다.
n, m = tuple(map(int, input().split()))
	
# m회에 걸쳐 동전의 위치를 입력받고 올바른 위치에 1을 표기합니다.
for i in range(m):
	r, c = map(int, input().split())
	arr[r][c] = i
			
for i in range(len(arr)):
	for j in range(len(arr)):
		print(arr[i][j], end=' ')
	print()
print()
for i in range(len(arr)):
	for j in range(len(arr)):
		if j == 3:
			arr[i-1][j-1] = i
			max_val = max(max_val, arr[i-1][j-1])

for i in range(len(arr)):
	for j in range(len(arr)):
		print(arr[i][j], end=' ')
	print()

print(max_val)
'''

'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque
dis = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1
            Q.append((nx, ny))
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
'''

'''
arr = list(map(int, input().split()))
res = [0] * len(arr)

for i in range(len(arr)):
    if 0 in arr:
        if arr[i] == 0:
            res[0:i] = reversed(arr[0:i])
            print(*res[:i])
            break
        else:
            continue    
    else:
        res[:len(res)] = arr[::-1]
        print(*res[:len(res)])
        break
'''


board = [
        [0 for _ in range(3)]
            for _ in range(3)         
         ]

n = 3
m = 3

dir_num = 0
left = 2
x, y = 1, 1
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

dis = [[0 for _ in range(3)]for _ in range(3)]

queue = deque()

for i in range(n):
    for j in range(n):
        if i == 0: 
            board[i][j] = i + 1
        elif i == 1:
            board[i][j] = j + 1
        else:
            board[i][j] = i + j
            board[(n // 2) - 1][(n // 2)] = 6
            
for i in range(n):
    for j in range(n):
        print(board[i][j], end= ' ')
    print()

nx = x + dx[dir_num] # 1 + 1 = 2
ny = y + dy[dir_num] # 2 + 0 = 2

right = 0
left_nx = x + dx[left]
right_nx = x + dx[right]


# x 조정 -> 상하  ///  y 조정 -> 좌우
print("처음 좌표 : %d %d \n값 : %d" % (x, y, board[x][y]))
print("오른쪽으로 이동 좌표 : %d %d\n값 : %d" % (right_nx, y, board[right_nx][y])) # 위로 이동 / x값을 1 증가 
print("왼쪽으로 감소 : %d %d \n값 : %d"% (left_nx, y, board[left_nx][y])) # 아래로 이동 x값을 1 감소
print()

print(board[0][1])
print(board[1][0])
print(board[1][2])
