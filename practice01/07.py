# a,b,c,d,e = input('입력:').split()

num = []

num1 = int(input('정수 입력1:'))
num.append(num1)
num2 = int(input('정수 입력2:'))
num.append(num2)
num3 = int(input('정수 입력3:'))
num.append(num3)
num4 = int(input('정수 입력4:'))
num.append(num4)
num5 = int(input('정수 입력5:'))
num.append(num5)

print('평균: {0}'.format(sum(num)/len(num)))