import sys 
sys.stdin = open("N과M4.txt","rt")

def dfs(L, idx):
    if L == m:
        for j in range(m):
            print(res[j], end= " ")
        print()
    else:
        for i in range(idx, n+1):
            res[L] = i
            dfs(L + 1, i)


n , m = map(int, map(int, input().split()))
res = [0] * (n + 1)
dfs(0, 1)