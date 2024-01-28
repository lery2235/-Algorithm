
import sys 
sys.stdin = open("대피소.txt", "rt")
INT_MAX = sys.maxsize
# "가장 멀리 떨어진 집과의 거리"
min_dis = INT_MAX

n, k = map(int, input().split())

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

coordinate = [list(map(int, input().split()))for _ in range(n)]

for i in range(n):
    for j in range(n-k):
        min_dis = min(min_dis, distance(coordinate[i], coordinate[j]))
print(min_dis)

