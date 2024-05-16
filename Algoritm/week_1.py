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

""" Lonely element
Given an array of element all elements repeats except one 
    return the element"""

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
def lonelyinteger(a):

    ## Time Complexity :- O(N), Space Complexity - O(N) using sets
    res = set()
    for num in a:
        if num in res:
            res.discard(num)
        else:
            res.add(num)
    for num in res:
        return num
    
    ## Time Complexity :- O(N), Space Complexity - O(1) using XOR operator
    res = 0
    for num in a:
        res ^= num
    return res


""" Diagonal difference
Given an 2D-array of element return the absolute 
difference of its left diagonal and right diagonal"""

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    LDS = 0
    RDS = 0
    for i in range(len(arr)):
        LDS += arr[i][i]
        RDS += arr[i][len(arr)-1-i]
    return abs(LDS - RDS)


# The function is expected to return a Encryptred STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            result += chr((ord(char)+k - 65)% 26 + 65)
            # as we the character to loop between A to Z
        elif char.islower():
            result += chr((ord(char)+k - 97)% 26 + 97)
            # as we the character to loop between a to z
        else:
            result += char
    return result

## Plaindrome index 
## Return the index by removing which the string is converted to palindrom 
def palindromeIndex(s):
    n, state, answer = len(s), True, -1
    SI, EI = 0, n-1
    while state:
        if (s[SI] == s[EI]):
            SI += 1
            EI -= 1
        elif (s[SI] != s[EI]):
            if (s[SI+1] == s[EI]):
                answer = SI
                state = False
            elif (s[SI] == s[EI-1]):
                answer = EI
                state = False
        if ((SI == n//2) or (EI == n//2)):
            state = False
    return answer

## Is the given grid of strings when sorted row wise
## is sorted column wise as well

def gridChallenge(grid):
    string_num = len(grid)
    string_len = len(grid[0])
    sorted_grid = []
    for i in range(0, string_num):
        sorted_chars = sorted(grid[i])
        sorted_grid.append(sorted_chars)
    for i in range(0, string_num-1):
        for j in range(0, string_len):
            if sorted_grid[i][j] > sorted_grid[i+1][j]:
                return 'NO'
    return 'YES'
