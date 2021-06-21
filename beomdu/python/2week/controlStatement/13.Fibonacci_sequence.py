# 13.피보나치 수열

index = 1
first_number = 0
secound_number = 0
while index < 51:
    if index < 3:
        print(1)
        first_number = 1
        secound_number = 1
    else:
        temp = first_number + secound_number
        print(temp)
        first_number = secound_number
        secound_number = temp
    index += 1
