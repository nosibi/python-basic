#chapter02-02
#파이썬 변수의 이해


#기본선언
n = 700

#출력

print(n)
print(type(n))

#동시선언
x = y = z = 700

#선언
var = 75

#재선언
var = "Change Value"

#출력
print(var)
print(type(var)) #마지막으로 선언한 것으로 됨

# Object References
# 변수값 할당 상태
# 1. 타입에 맞는 오브젝 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1
print(300)
print(int(300)) #외울필요는 없고 내부적으로 이렇게 작동한다~정도만

# 예2
n = 777
print(n,type(n))
print()

m = n # m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인: 객체의 고유값 확인
m = 800
n = 655

print(id(m)) #오브젝트의 고유값
print(id(n))
print(id(m) == id(n))
print()


# 같은 오브젝트 참조
m = 800
n = 800
z = 800
i = 800  # 파이썬이 효율성을 위해 하나의 존재로 규정

print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 다양한 변수 선언
# camel case : numberOfCollegeGraduates -> Method
# paskal case : NumberOfCollegeGraduates -> Class   별로 좋지는 않음
# snake case : number_of_college_graduates 추천하는 형태

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 8
1AGE = 9
#시작시 허용되는 특수문자는 _과 $ 등
# 숫자나 특수문자로 시작 안됨



# 예약어는 변수명으로 불가능(예약어는 이미 파이썬에서 쓰는 언어)
