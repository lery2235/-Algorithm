'''
4개의 숫자 [1, 5, 2, 6]이 주어졌을 때
이 중 서로 다른 2개의 숫자만 두 배로 해서, 인접한 숫자간의 차이의 합이 최대가 되도록 해보세요.
'''

n = 4
arr = [1, 5, 2 ,6]

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        arr[i], arr[j] = arr[i] * 2, arr[j] * 2 # 기존의 값 두 개를 두배 해서 위치를 교환

        sum_diff = 0 
        for k in range(n - 1):
            sum_diff += abs(arr[k + 1] - arr[k])

        max_sum = max(max_sum, sum_diff)
        arr[i], arr[j] = arr[i] // 2, arr[j] // 2

print(max_sum)
