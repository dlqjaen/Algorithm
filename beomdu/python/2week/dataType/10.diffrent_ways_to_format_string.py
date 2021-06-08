# 10.문자 포맷팅을 하는 다양한 방식

## 가장 오래된 방식 (%기호)
name = '이범두'
age = 20

print('제 이름은 %s이고 %d살입니다.' % (name, age))

## 현재 가장 많이 쓰이는 방식 (format 메소드)
print('제 이름은 {}이고 {}살입니다.'.format(name, age))

## 새로운 방식 (f-string) python3.6
print(f'제 이름은 {name}이고 {age}살입니다.')