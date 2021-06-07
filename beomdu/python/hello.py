print('Hello World!')

# --- 05 칼로리 계산기 ---
kitkat = 190
oreos = 502
pringles = 292
twix = 135.9
cheetos = 485

print(kitkat + oreos * 2)
print(pringles + twix * 2)

# --- 06 함수 ---
def hello():
    print("Hello!")
    print("Welcome to Codeit!")
hello()

# ---07 카페 모카 레시피 ---
def cafeMochaRecipe():
    print("1. 준비된 컵에 초코 소스를 넣는다.")
    print("2. 에스프레소를 추출하고 잔에 부어 준다.")
    print("3. 초코 소스와 커피를 잘 섞어 준다.")
    print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("5. 생크림을 얹어 준다.")
cafeMochaRecipe()

# ---08 파라미터 ---
def hello(name):
    print("Hello")
    print(name)
    print("Hello to Codeit!")
hello("Michael")

# ---09 여러 개의 파라미터 ---
def print_sum(a, b, c):
    print(a + b + c)
print_sum(7, 3, 2)

# ---10 세 수의 곱 ---
def multiply_three_numbers(a, b, c):
    print(a * b * c)

multiply_three_numbers(7, 3, 5)
multiply_three_numbers(21, 4, 9)
multiply_three_numbers(-7, 6, 3)

# ---11 return 문 ---
def get_square(x):
    return x * x
print(get_square(3))
y = get_square(3)
print(y)

# ---12 프로그래밍 기초 퀴즈 ---
## 질문 1
a = 5
b = 8
c = "5"
d = "8"

print(a + b) # 13

## 질문 2
print(c + d) # "58"

## 질문 3
def my_function(x, y):
    return x + x + y

print(my_function(10, 20)) # 40