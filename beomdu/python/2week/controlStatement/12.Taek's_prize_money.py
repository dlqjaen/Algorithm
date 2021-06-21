# 12.택이의 우승상금

year = 1989
money = 50000000
miran = 1100000000
while year != 2017:
    money += money*0.12
    year += 1
if (miran - money) < 0:
    print(f'{money - miran}원 차이로 동일 아저씨 말씀이 맞습니다.')
else:
    print(f'{miran - money}원 차이로 미란 아주머니 말씀이 맞습니다.')