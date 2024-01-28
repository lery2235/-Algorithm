import sys 
sys.stdin = open("1로 만들기", "rt")

x = int(sys.stdin.readline())
memo = [0] * (x + 1)

def devideToOne(x):

    if x == 1:
        return 0
    else:
        memo[x] = devideToOne(x - 1) + 1
        if x % 2 == 0:
            memo[x] = min(memo[x], devideToOne(x // 2) + 1)
        if x % 3 == 0:
            memo[x] = min(memo[x], devideToOne(x // 3) + 1)

    return memo[x]

print(devideToOne(x))



'''
n = 10
d = [0] * 1000001

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        #print("d[%d] : %d, d[%d // 2] : %d\n" % (i, i, d[i], d[i // 2]))
        d[i] = min(d[i], d[i//2] + 1)
        #print("변환 후 : d[%d] : %d, d[%d // 2] : %d\n" % (i, i, d[i], d[i // 2]))
    if i % 3 == 0:
        #print("d[%d] : %d, d[%d // 2] : %d\n" % (i, i, d[i], d[i // 2]))
        d[i] = min(d[i], d[i//3] + 1)
        #print("변환 후 : d[%d] : %d, d[%d // 2] : %d\n" % (i, i, d[i], d[i // 2]))
print(d[n])
'''