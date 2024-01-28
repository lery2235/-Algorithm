import sys
sys.stdin = open("BasicES4.txt", "rt")

def solution(n):
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i < j < k and arr[i] <= arr[j] <= arr[k]:
                    cnt += 1
    return print(cnt)


n = int(input())
solution(n)