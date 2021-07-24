# Chapter04-1
# 파이썬 제어문
# IF 실습

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



# 기본 형식
print(type(True)) # 0이 아닌 수, 문자, 데이터가 들어있는 리스트, 튜플...
print(type(False)) # 0, 빈 문자열, 빈 튜플, 빈 딕셔너리...

 # 예1
if True:
    print('Good')

if False:
    print('Bad')

# 에2
if False:
    print('Bad!')
else:
    print('Good')

# 관계 연산자
# >, >=, <, <=, ==, !=

x = 15
y = 10

# 양 변이 같은 경우 참
print(x == y)

# 양 변이 다를 떄
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클 떄 참
print(x < y)

# 오른쪽이 크거나 같을 떄 참
print(x <= y)

# 예3
city1 = ""
if city1:
    print("You are in :", city1)
else:
    print("please enter your city1")


city2 = "seoul"
if city2:
    print("You are in :", city2)
else:
    print("please enter your city2")


# 논리연산자
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c) # and는 둘다 True여야 True산술
print('or:', a > b or b > c)
print('not:', not a > b)
print('not:', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1:', 3+12 > 7+3)
print('e2:', 5+10*3 > 7+3*20)
print('e3:', 5+10 > 3 and 7+3 == 10)
print('e4:', 5+10 > 0 and not 7+3 == 10)

score1 = 70
score2 = 'A'

# 예4
# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 =='A' :
    print('Pass')
else:
    print('Fail')

# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
      print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')


# 예6
# 다중조건문

num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

# 예7
# 중첩조건문

grade = 'A'
total = 95

if grade =='A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')


# in, not if

q = [10, 20, 30] #리스트
w = {70, 80, 90, 100} #집합
e = {"name": "Lee", "city": "seoul", "grade": "A"} #딕셔너리
r = (10, 12, 14) #튜플

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("seoul" in e)
print("seoul" in e.values()) # seoul은 키가 아니라 값
