# Chapter03-2
#파이썬 문자형
#문자형 중요

#문자열 생성
str1 = 'I am python'
str2 = 'python'
str3 ='''How are you?'''
str4 = """Thank you!"""

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1)) #문자열 길이 함수(공백포함)

# 빈 문자열
str1_t1 = ''
str2_t2 = str() #위랑 같은 의미

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자 사용
# I'm boy

print("I'm boy")
#print('I'm boy) ->에러
print('I\'m boy') #이스케이프 형식

print('a \t b')
print('a \n b')
print('a \"\" b')


escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

#탭, 줄 바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)
print()

# Raw string 출력 (이스케이프와 반대)
raw_s = r'D:\python\test'
print(raw_s1)
print()

# 멀티라인 입력
multi_str1 = '''
string
Multi line
Test
'''
print(multi_str1)
print()

multi_str2 = \
'''
string
Multi line
Test
'''
print(multi_str2)


multi_str3 = \
'python' \
'java'\
'easy'
print(multi_str3)

# 문자열 연산
str_o1 = 'python'
str_o2 = 'apple'
str_o3 = 'How are you doing'
str_o4 = 'Seoul Deajeon Busan Jinju'

print(str_o1 *3)
print(str_o1 + str_o2)
print('y' in str_o1) #y라는 단어가 str_o1에 있는지?
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66),type(str(66))) #숫자가 아닌 문자66을 의미
print(str(10.1))
print(str(True),type(str(True)))


# 문자열 함수(upper, isalnum, startwith, count, endswith...)

print("capitalize:", str_o1.capitalize()) #시작문자를 대문자로 바꾸어줌
print("endswith?:", str_o2.endswith("s")) #끝글자가 s로 끝나는지
print("replace", str_o1.replace("thon", "Good"))
print("sorted: ", sorted(str_o1))
print("split:", str_o4.split(' ')) #공백을 기준으로 분리


# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__있으면 반복할 수 있음

#출력
for i in im_str:
    print(i)


# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))


# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2번째까지
print(str_s1[5:11])
print(str_s1[5:]) #[5:11]
print(str_s1[:len(str_s1)]) #str_sl[:11]
print(str_s1[:len(str_s1)-1]) #str_sl[:10]
print(str_s1[1:11:2])
print(str_s1[-5:]) # 마이너스는 오른쪽부터
print(str_s1[1:-1])
print(str_s1[::2])
print(str_s1[::-2])

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) #아스키코드 값을 알려주는 함수
print(chr(122)) #아스키코드를 알려주는 함수
