import sys
sys.stdin = open("DFS.txt", "rt")
#인접 리스트를 활용
#간선이 존재할 때만 배열에 추가

n, m = tuple(map(int, input().split()))
# 정점(n)과 간선(m) 입력

visited = [False for _ in range(n + 1)]
#방문처리
graph = [[] for _ in range(n + 1)]

vertext_cnt = 0

def dfs(vertex):
    global vertext_cnt

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertext_cnt += 1
            dfs(curr_v)

for i in range(m):
    v1, v2 = tuple(map(int, input().split()))
    # 1 2
    graph[v1].append(v2) # 2
    graph[v2].append(v1) # 1
print(visited[0])
visited[1] = True

dfs(1)

print(vertext_cnt)



