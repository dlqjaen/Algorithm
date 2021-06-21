print("5"+"8")
# %는 나머지, 나누기는 소수형★
# 버림 나눗셈
# 큰따옴표는 작은 따옴표로 감쌀 수 있다. print('가나다라 "마바사" 아자차') 이런식으로
#역슬래시(\) 사용하면 문자열 내에서 따옴표를 제대로 인식할 수 있다.
#.format -> {:.1f} :소수점 첫째자리까지만
print(7//2)
print(8//3)

print(float(3))
print(int("2")+int("5"))
print(str(2)+str(5))

age=7
print("제 나이는 " +str(age)+ "살입니다")
print("저는 {},{} 를 좋아합니다".format("유재석","박지성"))

num_1=1
num_2=3
print("{0} 나누기 {1}은 {2:.1f}입니다.".format(num_1,num_2,num_1/num_2))

#불대수의 연산 And(하나라도 거짓이면 거짓), or(하나라도 참이면 참), not(참이면 거짓, 거짓이면 참)

print(True and True)
print(2!=2)

print(type(4/2))

def hello(name):
    print(f"안녕하세요. {name}입니다")
    return "만나서 반갑습니다."
#return 없으면 none으로 나옴
print(hello("영훈"))

x=2
#글로벌 변수:함수밖에서 정의 ,모든 곳에서 사용 가능
def my_function():
    x=3
    #로컬변수 :함수내에서만 사용할 수 있는 변수/ 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고 나서 글로벌 변수를 찾음음    print(x)

my_function()
print(x)

#파라미터도 로컬 변수

#상수(constant) -되도록 대문자로 표시(바꾸지 않겠다는 뜻)
PI=3.14

#반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI*r*r
radius=4
print("반지름이 {}면, 넓이는 {}".format(radius,calculate_area(radius)))

#함수안에는 프린트문이 아닌 리턴문 사용

#추상화
#14.거스름돈 계산기
#yeonii
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
