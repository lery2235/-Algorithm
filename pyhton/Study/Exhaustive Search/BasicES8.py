import sys 
sys.stdin = open("BasicES8.txt", "rt")

INT_MIN =-sys.maxsize

'''

res = 0
binary_number = sys.stdin.readline().strip()
binary_number = [int(char) for char in binary_number]

for i in range(len(binary_number)):
    if binary_number[i] != 1:
        binary_number[i] = 1
        break
    else:
        continue

for i in binary_number:
    res = res * 2 + i

print(res)
'''
binary = list(map(int, list(input())))

ans = INT_MIN

for i in range(len(binary)):
    binary[i] = 1 - binary[i]

    num = 0
    for j in range(len(binary)):
        num = num * 2 + binary[j]
    ans = max(ans, num)

    binary[i] = 1 - binary[i]

print(ans)