year = 1988
prize_money = 5000
apart_price = 1100000000

while year <= 2016:
    interest = 5000 * (12 // 100)
    prize_money += interest

print(prize_money)

if prize_money > apart_price:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(prize_money - apart_price))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(apart_price - prize_money))