import re
from collections import Counter

def pwd_match(pwd):
    numbers = list(map(int, list(pwd)))
    sorted_pwd = sorted(numbers)
    return numbers == sorted_pwd and re.match(r".*(.)\1.*", pwd)

def pwd_match2(pwd):
    numbers = list(map(int, list(pwd)))
    sorted_pwd = sorted(numbers)
    return numbers == sorted_pwd and 2 in list(map(lambda x: x[1], Counter(numbers).items()))

def ex1():
    return len(list(filter(pwd_match, map(str, range(138241, 674035)))))

def ex2():
    return len(list(filter(pwd_match2, map(str, range(138241, 674035)))))


assert pwd_match('111111')
assert not(pwd_match('223450'))
assert not(pwd_match('123789'))
assert pwd_match2('112233')
assert not(pwd_match2('123444'))
assert pwd_match2('111122')

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())