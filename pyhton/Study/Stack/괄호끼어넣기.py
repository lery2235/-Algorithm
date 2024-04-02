import sys
sys.stdin = open("괄호끼어넣기.txt", "rt")

n = input()
stack = []
cnt = 0
# 스택에 남는 거는 ( 
# ) 이 카운팅
for i in n:
    if i == '(':
        stack.append(i)
    elif i == ')' and len(stack) != 0:
        stack.pop()
    else:
        cnt += 1

if len(stack) != 0:
    res = len(stack)     

print(res + cnt)