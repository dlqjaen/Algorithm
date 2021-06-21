# 05.옵셔널 파라미터

def myself(name, age, nationality='힌국'):
    print(f'내 이름은 {name}')
    print(f'내 나이는 {age}')
    print(f'국적은 {nationality}')

def myself(name, nationality='힌국',  age): # 옵셔널 파라미터는 마지막에 넣어야 함
    print(f'내 이름은 {name}')
    print(f'내 나이는 {age}')
    print(f'국적은 {nationality}')

myself('코드잇', 1,'미국')
print()
myself('코드잇', 1)

## SyntaxError: non-default argument follows default argument