import sys
sys.stdin = open("BasicES9", "rt")

INT_MAX = sys.maxsize

cpNumber = int(input())
arr = [list(map(int, input().split()))for _ in range(cpNumber)]
ans = INT_MAX
for i in range(1, cpNumber - 1):
    dist = 0
    prev_idx = 0
    for j in range(1, cpNumber):
        if j == i: # 같으면 스킵 그러니까 i = 1 j = 1 똑같은 구간은 스킵
            continue
        dist += abs(arr[prev_idx][0] - arr[j][0]) + abs(arr[prev_idx][1] - arr[j][1])
        prev_idx = j #리스트 번호 즉 체크포인트 번호를 알려줌
    
    ans = min(ans, dist)

print(ans)





