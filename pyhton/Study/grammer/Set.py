s1 = set({1, 2, 3})
s2 = set({1, 2, 3})
s3 = {1, 2, 3}
s4 = set()

'''
set 특징 
set으로 선언하게 되면 
새로 비어있는 set 객체 생성
 
1. 순서가 정해져 있지 않다.
2. 중복되지 않는 고유한 요소 

'''

#교집합(intersection 함수, &)
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(s1.intersection(s2))
print(s1 & s2)

#합집합
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(s1.union(s2))
print(s1 | s2)

#차집합
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(s1.difference(s2))
print(s2.difference(s1))

print(s1 - s2)
print(s2 - s1)
