# 문제2
# 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

# . : (dot) \n을 제외한 모든 문자 한 개와 매치
# * : 앞의 패턴이 0번 이상 반복됨을 의미
# +: 앞의 패턴이 1번 이상 반복됨을 의미
# ? : 앞의 패턴이 0번 혹은 1번 등장함을 의미 (={0,1})
# {m,n}: 앞의 패턴이 m번 이상 n번 이하 반복되는 걸 의미
# []: []안의 문자들 중 한 글자와 매칭됨, -를 통해서 범위를 나타낼 수 있음(ex> [a-zA-Z]: 모든 알파벳, [0–9]: 숫자)
# | : or 조건을 의미
# ^: 문자열의 시작을 의미
# $ : 문자열의 끝을 의미

import re

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

def remove_tag(con):
    x = re.compile('<.*?>')
    remove = re.sub(x,'',con)
    return remove

print(remove_tag(s))