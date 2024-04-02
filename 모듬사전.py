import sys 
sys.stdin = open("모듬사전.txt")

answer = 0
idx = -1 

def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(L, word_example):
        global answer,idx

        if L <= 5:
            idx += 1
            if word == word_example:
                answer = idx
        else:
            return
        
        for i in range(len(word)):
            dfs(L+1, word_example + word_list[i])
    
    dfs(0, '')
    
    return answer
word = input()
solution(word)