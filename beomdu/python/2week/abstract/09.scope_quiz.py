# 09.scope_quiz
## --- 01 ---
def my_function():
    x = '코드잇'
    x = '을지로'

my_function()
print(x) # 에러발생

## --- 02 ---
x = 100

def my_function():
    x = 0
    print(x) # 0

my_function()
print(x) # 100

## --- 03 ---
x = 10

def my_function():
    y = 5
    print(x + y) # 15

my_function()
print(x) # 10