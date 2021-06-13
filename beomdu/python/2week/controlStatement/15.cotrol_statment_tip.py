# 15.제어문 꿀팁

## break문
i = 100

while True:
    if i % 23 == 0:
        break
    i += 1
print(i)

## continue문
i = 0

while i < 15:
    i += 1

    if i % 2 == 1:
        continue
    print(i)