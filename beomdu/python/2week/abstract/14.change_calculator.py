# 14.거스름돈 계산기

def calculate_change(payment, cost):
    change = payment - cost

    five_million = change // 50000
    change = change - (five_million * 50000)

    one_million = change // 10000
    change = change - (one_million * 10000)

    five_thousand = change // 5000
    change = change - (five_thousand * 5000)

    one_thousand = change // 1000

    print(f'50,000원 {five_million}장')
    print(f'10,000원 {one_million}장')
    print(f'5,000원 {five_thousand}장')
    print(f'1,000원 {one_thousand}장')

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)