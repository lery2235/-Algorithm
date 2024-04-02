import sys 
sys.stdin = open("N과M.txt", "rt")


def dfs(L):
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print() 
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i 
                dfs(L+1)
                ch[i] = 0

n, m = map(int, input().split())
res = [0] * (n + 1)
ch = [0] * (n + 1)
dfs(0)