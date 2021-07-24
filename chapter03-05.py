# chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용(JSON)
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'Kim', 'phone': '01047685608', 'birth': '970623'}
b = {0: 'Hello Python'}
c = {'arr': [1,2,3,4]}
d = {
    'Name':'Niceman',
    'City':'Seoul',
    'Age' : 24,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name','Niceman'),
    ('City','Seoul'),
    ('Age' , 24),
    ('Grade', 'A'),
    ('Status', True)
]) # FM 방식, 어렵고 까다롭다

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a -',type(a), a)
print('b -',type(b), b)
print('c -',type(c), c)
print('d -',type(d), d)
print('e -',type(e), e)
print('f -',type(f), f)
print()

# 출력
print('a -',a['name']) # 존재x -> 에러발생
print('a -',a.get('name')) # 존재x -> None 처리
print('b -',b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))


# 딕셔너리 추가
a['address'] = 'seoul'
print('a -', a)

a['name'] = 'Lee'
print('a -', a)

a['rank'] = [1,2,3]
print('a -', a)

# 딕셔너리 길이
print('a -',len(a))
print('b -',len(b))
print('c -',len(c))
print('d -',len(d)) #키의 갯수, 길이

# dict_keys, dict_values, dict_items : 반복(__iter__)에서 사용 가능

print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys()) # 키만 가져오기

print('a -', list(a.keys()))
print('b -', list(b.keys()))

print()

print('a -', a.values())
print('b -', b.values())
print('c -', c.values())
print('d -', d.values()) # 값만 가져오기

print('a -', list(a.values()))
print('b -', list(b.values()))

print()

print('a -', a.items())
print('b -', b.items())
print('c -', c.items()) # 키랑 값 둘다 가져오기

print('a -', list(a.items()))
print('b -', list(b.items()))

print('a -', a.pop('name'))
print('a -', a)
print('c -', c.pop('arr'))
print('c -', c)

print()

print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)

print()

print('a -', 'birth' in a)
print('d -', 'City' in d)

# 수정
a['test'] = 'test_dict'

print('a -', a)

a['address'] = 'dj'
print('a -', a)

a.update(birth='981221')
print('a -', a)

temp = {'address': 'Busan'}
a.update(temp)
print('a -', a)
