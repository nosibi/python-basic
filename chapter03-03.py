#Chpater03-3
# 파이썬 리스트
# 자료구조에서 중요
#  리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine'] #서로 다른 자료형을 한 리스트 안에 가능
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'football',3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1][0])
print(type(e[-1][0]))

print(list(e[-1][0]))
print(type(list(e[-1][0]))) #list로 형 변환


# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d -', d[2:])
print('e -', e[-1][1:3])


# 리스트 연산 (집합 + 집합 = 집합)
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3) #순서는 유지
print("'Test' + c[0]", 'Test' + str(c[0])) # 리스트형을 문자형으로 변환 후 연산

# 값 비교
print(c[:3])
print(c[3:])

print(c == c[:3] + c[3:]) #0,1,2 -> 3개의 인덱스 + 3번째 인덱스
print(c)
print(c[:3] + c[3:])
print()
# Identity(id)

temp = c
print(temp,c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c'] #[['a', 'b', 'c']]
print('c -', c)
c[1] = ['a', 'b', 'c']
print('c -', c)
c[1:3] = []
print('c -', c)
del c[2] #삭제
print('c -', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a -', a)

a.append(6) #삽입
print('a -', a)

a.sort()
print('a -', a)

a.reverse()  # 역순
print('a -', a)

print('a -', a.index(3)) # 리스트에서 3이라는 숫자의 위치 찾기
print('a -', a[3])

a.insert(2, 7)
print('a -', a)

a.reverse()
print('a -', a)

# del a[6]
# print('a -', a)
a.remove(6) #불필요한 데이터를 리스트에서 제거
print('a -', a)

print('a - ',a.pop()) # 마지막꺼 추출
print('a -', a)

print('a - ',a.pop())
print('a -', a)

print('a -',a.count(4)) # 4가 리스트안에 몇개가 있지?

ex = [8,9]
a.extend(ex)
print('a -', a)

# 삭제: remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
