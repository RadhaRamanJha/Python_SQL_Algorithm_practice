from datetime import date
import calendar
month_length = [31,28,31,30,31,30,31,31,30,31,30,31]
key_array = ["January", "February", "March", "April", "May", "June", "July", 
             "August", "September", "October", "November", "December"]
# Using List
def print_month(month, year):
    idx = key_array.index(month)
    day = 1
    wd = date(year,idx+1,day).weekday()
    wd = (wd+1)%7
    end = month_length[idx]
    if calendar.isleap(year) and idx == 1:
        end += 1
    print('{} {}'.format(month,year).center(20))
    print('Su Mo Tu We Th Fr Sa')
    print("   "*wd,end='')
    while day <= end:
        print('{:2d} '.format(day),end='')
        wd = (wd+1)%7
        day += 1
        if wd == 0:
            print()
    print()
print_month("September",2024)

## Convert word to Integer to base 26
def base26(w):
    val = 0
    for ch in w.lower():
        next_digit = ord(ch) - ord('a')
        val = 26*val+next_digit
    return val
print(base26("June"))

# Creation of unique_key for every month
day_array = [base26(month)%34 for month in key_array]
print(day_array)