# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

i = [10,12,14,15,17,18,19,20,25,30,32,33,40,43,44,46,50]
a = []
for j in i:
    if (int(j) %3) == 0:
        a.append(j)

print('주어진 리스트에서 3의 배수의 개수: {0}'.format(len(a)))
print('주어진 리스트에서 3의 배수의 합: {0}'.format(sum(a)))
