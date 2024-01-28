import sys 
sys.stdin = open("듣보잡.txt", "r")

n, m = map(int, input().split())
L = set([input().strip() for _ in range(n)])
S = set([input().strip() for _ in range(m)])

res = sorted(L & S)

cnt = len(res)
print(cnt)

for i in res:
    print(i)


