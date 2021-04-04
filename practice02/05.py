#

def mysum(*num):
    result = 0
    for i in num:
        result += i

    return result


print(mysum())
print(mysum(1, 2))
print(mysum(1, 2, 5, 7, 2, 3))