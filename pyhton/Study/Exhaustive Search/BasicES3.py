import sys
sys.stdin = open("BasicES3.txt", "rt")


def solution(string, n):
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if string[i] == '(' and string[j] == ')':
                count += 1
        

    return print(count)


string = input()
n = len(string)

solution(string,n)