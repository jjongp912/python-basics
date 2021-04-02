
money = int(input('금액: '))


a = money // 50000
money = money - 50000 * a
print('50000원: {0}개'.format(a))
b = money // 10000
money = money - 10000 * b
print('10000원: {0}개'.format(b))
c = money // 5000
money = money - 50000 * c
print('5000원: {0}개'.format(c))
d = money // 1000
money = money - 1000 * d
print('1000원: {0}개'.format(d))
e = money // 500
money = money - 500 * e
print('500원: {0}개'.format(e))
f = money // 100
money = money - 100 * f
print('100원: {0}개'.format(f))
g = money // 50
money = money - 50 * g
print('50원: {0}개'.format(g))
h = money // 10
money = money - 10 * h
print('10원: {0}개'.format(h))
i = money // 5
money = money - 5 * i
print('5원: {0}개'.format(i))
j = money // 1
money = money - 1 * j
print('1원: {0}개'.format(j))