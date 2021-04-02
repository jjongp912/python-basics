num = int(input('숫자를 입력하세요: '))
a=[]
b=[]
for i in range(num+1):
    if (i%2) == 0:
        a.append(i)
    else :
        b.append(i)
if (i%2) == 0:
    print('결과 값: {0}'.format(sum(a)))
else:
    print('결과 값: {0}'.format(sum(b)))