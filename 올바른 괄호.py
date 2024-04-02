import sys 
sys.stdin = open("올바른 괄호.txt", "rt")

stack =[]
s = input()

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    if s[i] == ')' and len(stack) != 0:
        stack.pop()

if len(stack) != 0:
    print("false")  
