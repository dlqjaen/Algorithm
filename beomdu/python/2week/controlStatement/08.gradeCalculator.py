# 08.학점 계산기

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score

    if total >= 90:
        return print('A')
    if total >= 80:
        return print('B')
    if total >= 70:
        return print('C')
    if total >= 60:
        return print('D')
    return print('F')

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)