# 이상한 수학 문제2

i = 1
j = 0
while i < 1000:
    if (i%2 == 0) | (i%3 == 0):
        j += i
    i += 1
print(j)