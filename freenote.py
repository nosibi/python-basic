import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


sum1 = 0

for v in range(1, 1001):
    sum1 = sum1 + v

print("1 ~ 1000 sum :", sum1)

print()

print("4의 배수의 합 :", sum(range(1, 10001, 4)))

for v2 in range(4, 11):
    print("number is", v2)

print()

names = ['Kim', 'Lee', 'Choi']
for k in names:
    print('name is', k)

print()

word = "earth"

for w in word:
    print('word :', w)

print()

my_info = {
      "Name" : "Lee",
      "Age" : 23,
      "City" : "Seoul"
}

for k in my_info.values():
    print("info :", k)
