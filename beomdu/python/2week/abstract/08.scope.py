# 08.scope

def my_function():
    x = 3 # 로컬 변수
    print(x)

my_function()
print(x)

# ----------

x = 2 # 글로벌 변수
def my_function():
    print(x)

my_function()
print(x)

# ----------

x = 2 # 글로벌 변수
def my_function():
    x = 3 # 로컬 변수
    print(x) # 3

my_function()
print(x) # 2

# ----------

def squire(x): # 파라미터도 로컬변수
    return x * x

print(squire(3))