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

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
# e.g :- 
    # superDigit(p) = superDigit(9875987598759875)
    #               9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    # superDigit(p) = superDigit(116)
    #               1+1+6 = 8
    # superDigit(p) = superDigit(8)

def superDigit(n, k):
    temp = 0
    for char in n:
        temp += int(char)
    p = temp*k
    if (len(str(p)) == 1):
        return p
    else:
        if p % 9 == 0:
            return 9
        else:
            return p % 9
# problem involves determining the minimum number of bribes required to transform a queue of people into its current state,
# where each person can bribe at most two others to move ahead.
# If any person has moved more than two positions forward, the situation is deemed "Too chaotic"
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                bribes += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif q[i-2] == i+1:
                bribes += 2
                q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
            else:
                print("Too chaotic")
                return
    print(bribes)

# determining the starting petrol pump index from which a truck can complete a circular tour of petrol pumps. 
# Each pump provides a certain amount of petrol and the truck consumes a certain amount of petrol to travel to the next pump. 
# The goal is to find the starting pump index where the truck can complete the entire tour without running out of petrol.

def truckTour(petrolpumps):
    start_position, fuel = 0, 0
    for i in range(len(petrolpumps)):
        fuel += petrolpumps[i][0] - petrolpumps[i][1]
        if fuel <= 0:
            start_position = i+1
            fuel = 0
    return start_position

# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. 
# Complete the mergeLists function, which returns a pointer to the head of the merged list. The function should handle cases where either or both input lists are empty.


def mergeLists(head1, head2):
    # case when both head point null
    if head1 is None and head2 is None:
        return None
    # case when one head points to null
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    # General case
    if head1.data < head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    # if both head data are equal the mutual order in which they appear doesnot matter
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)
    return temp

# Implement a queue using two stacks and process a series of queries:

# Enqueue an element into the queue.
# Dequeue the front element from the queue.
# Print the front element of the queue.
# Each query will be one of these three types, provided with relevant values if necessary.

q = int(input())
stack_push = []
stack_delete = []
for i in range(q):
    i = list(input().split())
    if i[0] == '1':
        stack_push.append(i[1])
    elif i[0] == '2':
        popped_item = stack_push.pop(0)
    elif i[0] == '3':
        print(stack_push[0])

# Given a string of brackets among ('(' , ')', '{', '}', '[', ']'), determine if it is balanced. 
# A sequence is balanced if each opening bracket has a corresponding closing bracket in the correct order.
# Implement the function isBalanced to return YES or NO

def isBalanced(s):
    opened_brackets = []
    closing_brackets = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in ['(', '{', '[']:
            opened_brackets.append(char)
        else:
            if opened_brackets:
                current_bracket = opened_brackets.pop()
                if closing_brackets[current_bracket] != char:
                    return 'NO'
            else:
                return 'NO'
    return 'NO' if opened_brackets else 'YES'