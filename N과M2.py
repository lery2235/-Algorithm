import sys 
sys.stdin = open("N과M2.txt", "rt")


def dfs(L, idx):
    if L == m:
        for j in range(m):
            print(res[j], end= " ")
        print()
    else:
        for i in range(idx, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L + 1, i + 1)
                ch[i] = 0


n, m = map(int, input().split())
ch = [0] * (n + 1)
res = [0] * (n + 1)
dfs(0, 1)