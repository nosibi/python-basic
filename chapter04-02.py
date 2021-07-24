import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Chapter 04-2
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(10):    # 0~9
    print('v1 is :', v1)

for v2 in range(1, 11): # 1~10
    print('v2 is :', v2)


for v3 in range(1, 11, 2):
    print('v3 is :', v3)

# 1 ~ 1000까지의 합

sum1 = 0

for v in range(4, 1001, 4):
    sum1 = sum1 + v     # sum1 += v 로도 가능

print('1 ~ 1000 sum1 :', sum1)

print('1 ~ 1000 sum2 :', sum(range(1,1001)))

print()
print(' 1 ~ 1000, 4의 배수의 합 :', sum(range(4, 1001, 4)))

# Iterables 자료형
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name)


# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Currnet number : ", n)


# 예제3
word = "Beautiful"

for s in word:
    print('word :', s)

# 예제4
my_info = {
      "name" : "Lee",
      "Age" : 33,
      "City" : "Seoul"
}

for k in my_info:
    print('key:', k)

print()


my_info = {
      "name" : "Lee",
      "Age" : 33,
      "City" : "Seoul"
}

for k in my_info:
    print('key:', my_info[k]) #my_info.get(k)

for v in my_info.values():
    print('value :', v)


# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 10:
        print('Found : 10!')
        break  # 값을 찾으면 정지(if문에서 많이 사용된다)
    else:
        print('Not found :', num)

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue # 해당되는 부분을 스킵
    print("current type:",v ,type(v))
