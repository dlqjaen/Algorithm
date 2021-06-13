# 11.약수 찾기

i = 1
j = 0
while i < 121:
    if 120%i == 0:
        print(i)
        j += 1
    i += 1
print(f'120의 약수는 총 {j}개 입니다.')