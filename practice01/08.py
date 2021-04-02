#
def reverse(s):
    s = list(s)
    t = []
    for i in s[::-1]:
        t.append(i)
    print(''.join(t))



instr = str(input('입력>'))
reverse(instr)

