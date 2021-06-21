#추상화
#14.거스름돈 계산기

def calculate_change(payment, cost):
    change = payment-cost
    a = change//50000
    b = (change-50000*a)//10000
    c = (change-50000*a-10000*b)//5000
    d = (change-50000*a-10000*b-5000*c)//1000
    print("50000원 지폐 : {}장".format(a))
    print("10000원 지폐 : {}장".format(b))
    print("5000원 지폐 : {}장".format(c))
    print("1000원 지폐 : {}장".format(d))


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

#변수이름 잘 정의(fifty_count등)
#%이용하기