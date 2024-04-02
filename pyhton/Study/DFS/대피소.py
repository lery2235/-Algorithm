
import sys 
sys.stdin = open("대피소.txt", "rt")
INT_MAX = sys.maxsize
# "가장 멀리 떨어진 집과의 거리"
min_dis = INT_MAX

n, k = map(int, input().split())
answer = INT_MAX

def go():
    global answer 
    max_dis = 0
    for i in range(n):
        if visited[i] == False:
            min_dis = INT_MAX
            for j in range(k):
                index = array[j] # 대피소 index
                dis = abs(coordinate[i][0] - coordinate[index][0]) + abs(coordinate[i][1] - coordinate[index][1]) # 거리
                min_dis = min(min_dis, dis) # 1번 대피소 거리 구하고 최소값 비교 2번 대피소 거리 구하고 최소값 비교
                #1 2 번 중 거리가 최소 인 것  
            max_dis = max(max_dis, min_dis) # 전체 좌표에서 거리가 제일 긴 거
    answer = min(answer, max_dis)
    

def dfs(depth, idx): #여기로 
    if depth == k:
        go()
        return
    else:
        for i in range(idx, n): 
            if visited[i] == False:
                array[depth] = i
                visited[i] = True
                dfs(depth + 1, i + 1)
                visited[i] = False


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

visited = [False] * (n + 1)
coordinate = [list(map(int, input().split()))for _ in range(n)]
array = [0] * (k + 1)
dfs(0, 0)

print(answer)