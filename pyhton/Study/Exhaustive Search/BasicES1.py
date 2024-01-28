import sys 
sys.stdin = open("sec.txt", "rt")

INT_MAX = sys.maxsize
n = int(input())
    
def soultion(n):
    arr = list(map(int, input().split()))
    min_dist = INT_MAX
    
    for i in range(n):    
        sum_dist = 0 #이동거리의 합
        for j in range(n):
            sum_dist += abs(j - i) * arr[j]
    

    
    min_dist = min(min_dist, sum_dist)
    return print(min_dist)
    

soultion(n)







