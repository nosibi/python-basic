# chapter03-1
# 숫자형

# 파이썬 지원 자료형(암기x)
"""
int:정수
float:실수
complex:복소수
bool: 불린 ->true or false
str:문자열(시퀀스)
list:리스트(시퀀스)
tuple:튜플(시퀀스)#시퀀스는 반복을 처리가능, 순서를 기다리는것
set:집합
dict:사전
"""

# 데이터 타입(괄호가 다 다르다)
str1 = "python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 = 10.0 ? 다르다!
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0 #2.0을 알기 위해서느 version이라는 키 필요
}
tuple = (7, 8, 9)
set = {3, 5, 7}
# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))



# 숫자형 연산자
"""
+
-
*
/
//:몫
%:나머지
abs(x):절댓값
pow(x, y): x의 y제곱 계 x ** y -> 2 ** 3
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777799999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print(i+i2)

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()


# 연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777897878978
big_int2 = 1231231241341231231123
f1 = 1.234
f2 = 3.939

# +
print(">>>>>+")
print("i1 + i2 :", i1 + i2)
print("f1 + f2 :", f1 + f2)
print("big_int1 + big_int2 : ",big_int1 + big_int2)


# *
print(">>>>>+")
print("i1 * i2:", i1 * i2)
print("f1 * f2:", f1 * f2)
print("big_int1 * big_int2 : ",big_int1 * big_int2)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1 , false : 0
print(float(False)) # 0.0
print(complex(3))
print(complex('3')) #문자형->숫자형
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x , y = divmod(100,8) #몫과 나머지

print(x,y)
print(pow(5,3), 5**3)

#외부모듈

import math  # math라는 파일 호

print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정
print(math.pi)
