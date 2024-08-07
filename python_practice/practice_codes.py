def revers_integer(num):
    if num < 0:
        sign = -1
    elif num > 0:
        sign = 1
    else:
        sign = 0
    abs_num = abs(num)
    reverse = 0
    while abs_num != 0:
        reverse = reverse*10 + abs_num % 10
        abs_num = abs_num // 10
    print(reverse*sign)
revers_integer(-12345)