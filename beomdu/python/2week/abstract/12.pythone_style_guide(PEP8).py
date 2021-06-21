# 12.파이썬 스타일 가이드 (PEP 8)

### 이름 -------------------
## --- 이름 규칙 ---
# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good
some_variable_name = 1

def some_function_name():
    print("Hello")

# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14

## --- 의미있는 이름 ---
# bad
a = 2
b = 3.14
print(b * a * a)

# good
radius = 2
pi = 3.14

print(pi * radius * radius)

# bad
def do_something():
    print("Hello, world!")

# good
def say_hello():
    print("Hello, world!")

### 화이트 스페이스 -------------------
## --- 들여쓰기 ---
# bad
def do_something():
  print("Hello, world!")

i = 0
while i < 10:
        print(i)

# good
def say_hello():
    print("Hello, world!")

## --- 함수 정의 ---
# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')

# good
def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

## --- 괄호안 ---
# bad
spam( ham[ 1 ], { eggs: 2 } )

# good
spam(ham[1], {eggs: 2})

## --- 함수 괄호 ---
# bad
def spam (x):
    print (x + 2)

spam (1)

# good
def spam(x):
    print(x + 2)

spam(1)

## --- 쉼표 ---
# bad
print(x , y)

# good
print(x, y)

## --- 지정 연산자 ---
# bad
x=1
x    = 1

# good
x = 1

## --- 연산자 ---
# bad
i=i+1
submitted += 1

# good
i = i + 1
submitted += 1

# bad
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# good
x = x*2 + 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

## --- 코멘트 ---
# bad
x = x + 1# 코멘트

# good
x = x + 1  # 코멘트