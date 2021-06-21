# 07.elif문

score = 34
if score > 70:
    print('A를 준다.')
else:
    if score > 60:
        print('B를 준다')
    else:
        if score > 50:
            print('C를 준다')
        else:
            if score > 40:
                print('D를 준다')
            else:
                print('F를 준다')

if score > 70:
    print('A를 준다.')
elif score > 60:
    print('B를 준다.')
elif score > 50:
    print('C를 준다.')
elif score > 40:
    print('D를 준다.')
else:
    print('F를 준다.')