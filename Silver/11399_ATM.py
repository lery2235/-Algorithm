import sys
sys.stdin=open("11399.txt", "r")

n = int(input())
P = list(map(int, input().split()))
hap = 0
res = []
answer = 0

P.sort()

for i in range(n):
    hap = hap + P[i]
    res.append(hap)

for i in res:
    answer += i

print(answer)
