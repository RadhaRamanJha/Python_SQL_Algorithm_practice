# Min-max problem - Given an array resturn the total_possitve_num/len_array , zero_num/len_array , total_negative_num/len_array 

def plusMinus(arr):
    pos_num, neg_num, zero = 0, 0, 0
    total_num = len(arr)
    for num in arr:
        if num > 0:
            pos_num += 1
        elif num < 0:
            neg_num += 1
        else:
            zero += 1
    print(pos_num/total_num)
    print(neg_num/total_num)
    print(zero/total_num)

# Given five possitive numbersin an array find the minimum and maximum values that can be calculated by summing
# exactly four out of the five numbers. Then print the respective minimum and maximum values as a single line of
# two space seperated long integers

def miniMaxSum(arr):
    sum = 0
    min_num, max_num = arr[0], arr[0]
    for num in arr:
        sum += num
        if num <= min_num:
            min_num = num
        elif num >= max_num:
            max_num = num
    
    print(f'{sum-max_num} {sum-min_num}')

# Conversion time from 12 hour format to 24 hour format
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    if s[8:] == 'PM':
        if int(s[:2]) == 12:
            res_hr = str(12)
        else:
            res_hr = str(int(s[:2])+12)
    elif s[8:] == 'AM':
        if int(s[:2]) == 12:
            res_hr = str(00)
        else:
            res_hr = s[:2]
    res = res_hr+s[2:8]
    return res