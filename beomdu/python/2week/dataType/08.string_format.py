# format을 이용한 문자열 포맷팅

year = 2021
month = 6
day = 8

print('오늘은 ' + str(year) + '년 ' + str(month) + '월 ' + str(day) + '일 입니다.')

day_string = '오늘은 {}년 {}월 {}일 입니다.'
print(day_string.format(year, month, day))