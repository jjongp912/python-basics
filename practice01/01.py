# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요.
import sys

number = input('수를 입력하세요:')

s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


for i in list(number):
    for j in s:
        if i == j:
            print('정수가 아닙니다.')
            sys.exit()

if int(number)%3 == 0:
    print('3의 배수 입니다.')
else :
    print('3의 배수가 아닙니다.')
