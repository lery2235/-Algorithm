import sys 
sys.stdin = open("다리놓기.txt", "rt")
'''
def dfs(L, idx):
    global cnt
    if L == n:
        cnt += 1
    else:
        for i in range(idx, m): 
            if ch[i] == 0:
                ch[i] = 1
                dfs(L+1, i+1)
                ch[i] = 0
T = int(input())

for i in range(T):
    cnt = 0
    n, m = map(int, input().split())
    ch = [0] * (m + 1)
    dfs(0, 0)
    print(cnt)

'''

n, m = 