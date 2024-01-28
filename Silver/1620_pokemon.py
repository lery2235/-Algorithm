import sys 
sys.stdin = open("1620.txt", "r")
#enumerate 
#순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
#인덱스와 값을 동시에 접근하면서 루프를 돌리고 싶을 때 사용

n, m = map(int, input().split())
pokemon = {}
pokemon_id = {}

for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    pokemon[i] = name 
    pokemon_id[name] = i
 
for _ in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit() == True:
        print(pokemon[int(question)])
    else:
        print(pokemon_id[question])
     