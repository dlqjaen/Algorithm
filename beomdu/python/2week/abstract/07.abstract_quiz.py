# 07.추상화 퀴즈
## --- 1 ---
x = -6
y = 3

x += 2
y -= 1

print(x + y) # -2

## --- 2 ---
def hello(name):
    print(f"안녕하세요. {name}입니다.") # 2
    print("만나서 반갑습니다.") # 3


print("함수 실행 전") # 1
hello("영훈")
print("함수 실행 후") # 4

## --- 3 ---
def hello(name):
    print(f"안녕하세요. {name}입니다.") # 1
    return "만나서 반갑습니다."

print(hello("영훈")) # 2