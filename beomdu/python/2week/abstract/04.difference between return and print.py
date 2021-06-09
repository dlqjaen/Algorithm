# 04.return과 print의 차이
def print_square(x):
    print(x * x)

def get_squire(x):
    return x * x

get_squire(3) #
print(get_squire(3)) # 9
print(print_square(3)) # 9, None