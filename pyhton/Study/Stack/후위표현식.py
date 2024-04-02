import sys 
sys.stdin = open("후위표현식.txt", "rt")

prec = {'*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1 }

s = input()
stack = []
answer = ''

for formula in s:
    if formula.isalpha():
        answer += formula
    else:
        if formula == '(':
            stack.append(formula)
        
        elif formula == ')':
            while len(stack) != 0 and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        
        elif formula in prec:
            while len(stack) != 0 and prec[stack[-1]] >= prec[formula]:
                answer += stack.pop()
            stack.append(formula)
            
while len(stack) != 0:
    answer += stack.pop()

print(answer)
    
    
    