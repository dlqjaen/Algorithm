# 11.스타일

print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)

# ----------------

PI = 3.14 # 원주율(파이)

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

# PEP8 파이썬 스타일 가이드