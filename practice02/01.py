# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서
# 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

x = s.split('/')
print(x[1:])
# 또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.

x.reverse()
y = x[1:]
print(x[0])
print(f'{"/".join(y[::-1])},  {x[0]}')
