#chapter02-1
#print 사용법
#참조 http://www.python-course.eu/python3_formatted_output.php

#기본출력
print('python start!')
print("python start!")
print()
print()
print('''python start!''')
print("""python start!""")
print()

#separator 옵션
print('P','Y','H','O','N')
print('P','Y','H','O','N',sep='')
print('P','Y','H','O','N',sep=',')
print('010','7777','1234',sep='-')

#end 옵션(다음 print문을 칸을 띄지 않고 연결)
print('welcome to',end=' ')
print('IT News',end=' ')
print('web site')

#file 옵션(이런게 있다는 정도만 알아두기)
import sys
print('Learn Python',file=sys,stdout)
print()

# format 사용(d : 3, s : 'python'(문자열), f : 3.144545)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','2'))
print('{1} {0}'.format('one','2')) #0,1,2,3...순으로 우선순위




# %$

print('%10s' % ('nice')) #왼쪽부터 공백으로 채움 #%는 자릿수 의미
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) #중앙정렬

print('%5s' % ('nice'))
print('%.5s' % ('pythonsyudy'))#5글자만 절삭
print('{:10.5}'.format('pythonstudy'))#10개 공간 확보 5글자만

# %d(정수일경우)


print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (12))
print('{:4d}'.format(12))

#%f(실수일경우)

print('%f' % (3.14159287))
print('%1.8f' % (3.14159287))

print('%06.2f' % (3.14159287))
print('{:06.2f}'.format(3.14159287))
