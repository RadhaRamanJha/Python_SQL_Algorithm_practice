"""
Q1. 

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    lis1 = []
    for i in range(N):
        instruct = input()
        if 'insert' in instruct:
            numb = instruct.split()
            lis1.insert(int(numb[1]),int(numb[2]))
        elif 'print' in instruct:
            print(lis1)
        elif 'remove' in instruct:
            numb = instruct.split()
            lis1.remove(int(numb[1]))
        elif 'append' in instruct:
            numb = instruct.split()
            lis1.append(int(numb[1]))
        elif 'sort' in instruct:
            lis1.sort()
        elif 'pop' in instruct:
            lis1.pop()
        elif 'reverse' in instruct:
            lis1.reverse()


"""
Draw the Pattern :- 
      H      
     HHH     
    HHHHH    
   HHHHHHH   
  HHHHHHHHH  
 HHHHHHHHHHH 
HHHHHHHHHHHHH
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
                            HHHHHHHHHHHHH 
                             HHHHHHHHHHH  
                              HHHHHHHHH   
                               HHHHHHH    
                                HHHHH     
                                 HHH      
                                  H   

"""
def pattern_H(n:int): # n must be Odd number only .
    thickness = n
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

pattern_H(7)

"""
Designed a new door mat with the following specifications:

Mat size must be N X M. ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

"""

n, m = list(map(int, input().split()))
for i in range(1, n+1, 2):
    if i < n:
        current_char = i*'.|.'
    else:
        current_char = 'WELCOME'
    print(current_char.center(m, '-'))
for j in range(n-2, 0, -2):
    current_char = j*'.|.'
    print(current_char.center(m, '-'))

"""
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""
def string_val():
    s = input()
    a = any(x.isalnum() for x in s)
    b = any(x.isalpha() for x in s)
    c = any(x.isdigit() for x in s)
    d = any(x.islower() for x in s)
    e = any(x.isupper() for x in s)
    print(f"{a}\n{b}\n{c}\n{d}\n{e}")

"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
Input Format

The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
"""
score_list=[]   # empty list to store scores
records=[]      # empty list of lists to store scorers and scores
name_list=[]    # empty list to store scorers

# Take name and score inputs from user
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append(score)
    records.append([name, score])

unique_scores=list(set(score_list))
unique_scores.sort()  # Sort the list of unique scores

for name, score in records:
    if score==unique_scores[1]:
        name_list.append(name)

name_list.sort()  # Sort the name list of scorers
for name in name_list:
    print(name)

"""
Given an integer n, print each integer from 1 to n in decimal, 
octal, hexadecimal (capitalized), and binary formats. 
Each value should be space-padded to align with the width of the binary representation of n.
"""

def print_formatted(number):
    width = len(bin(number))-2
    for i in range(1, number+1):
        print(str(i).rjust(width), end=" ")
        print(oct(i)[2:].rjust(width), end=" ")
        print(hex(i)[2:].upper().rjust(width), end=" ")
        print(bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
"""
The problem involves generating all possible permutations of a given string of length n in lexicographic sorted order.
 Given a string S and an integer k, the task is to print all possible permutations of length k from the string S. The output should list each permutation on a new line.

"""
from itertools import permutations
prompt = list(input().split())
results = list(permutations(str(prompt[0]), r=int(prompt[1])))
for res in sorted(results):
    print("".join(res))

"""
The problem involves generating the Cartesian product of multiple input iterables using the itertools.product function.
Given two lists, A and B, the task is to print all possible pairs (Cartesian product) formed by taking an element from A and an element from B. 
The output should display each pair on a single line in lexicographic sorted order.
"""
from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
products = product(a, b)
for item in products:
    print(item, end=" ")

"""
The problem involves managing a shoe store's inventory and fulfilling customer requests for specific shoe sizes at varying prices. 
By utilizing collections.Counter, one can efficiently track the available shoe sizes and their counts. 
Processing each customer's request with this counter allows calculating the total revenue earned from selling the shoes.
"""
number_of_shoe = int(input())
shoe_sizes = []
for i in input().split(" "):
    shoe_sizes.append(int(i))
money_earned = 0
total_customers = int(input())
while total_customers > 0:
    customer_dem = input().split(" ")
    if int(customer_dem[0]) in shoe_sizes:
        money_earned += int(customer_dem[1])
        shoe_sizes.remove(int(customer_dem[0]))
    total_customers -=1
print(money_earned)
"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .
"""
def solve(s):
    splitted_names = s.split()
    cap_names = [s1.capitalize() for s1 in splitted_names]
    return " ".join(cap_names)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
"""
Calculate the ratio of
sum of distimct height to
number of distinct height
"""

def average(array):
    array_num = len(set(array))
    total = 0
    for num in set(array):
        total += num
    return round(total/array_num, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
"""
Given an input complex number convert it into 
polar coordinates
"""
import cmath
comp_num = complex(input())
print(abs(comp_num))
print(cmath.phase(comp_num))

"""
You are given two values a and b.
Perform integer division and print a//b .

Input Format

The first line contains , the number of test cases.
The next  lines each contain the space separated values of a and b.

"""

n = int(input())
for _ in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e) 
    except ValueError as e: 
        print("Error Code:", e)
"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B .

If set A  is subset of set B, print True.
If set A is not a subset of set B , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Constraints

Output Format

Output True or False for each test case on separate lines.

"""

num_test_cases = int(input())
while num_test_cases > 0:
    set_a_num = int(input())
    set_a = set(map(int, input().split()))
    set_b_num = int(input())
    set_b = set(map(int, input().split()))
    if (set_a_num < set_b_num) and set_a.issubset(set_b):
        print(True)
    else:
        print(False)
    num_test_cases -= 1
"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the  sets.

Print True, if A is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

"""

super_set = set(map(int, input().split()))
num = int(input())
result = True
while num:
    chk_set = set(map(int, input().split()))
    if not super_set.issuperset(chk_set):
        result = False
        break
    num -= 1
print(result)
"""
Task
Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Output Format

Output total number of students who have subscriptions to the English or the French newspaper but not both.
"""

eng_stud_num = int(input())
eng_stud_roll = set(map(int, input().split()))
frc_stud_num = int(input())
frc_stud_roll = set(map(int, input().split()))
print(len(eng_stud_roll ^ frc_stud_roll))

"""
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
"""

set_m_num = int(input())
set_m = set(map(int, input().split()))
set_n_num = int(input())
set_n = set(map(int, input().split()))
res = sorted(list((set_m - set_n) | (set_n - set_m)))
for num in res:
    print(num)

"""
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer A, the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

 0 < len(set(A)) < 1000
 0 < len(otherSets) < 100
 0 < N < 100

Output Format

Output the sum of elements in set A.

"""

set_A_num = int(input())
set_A = set(map(int, input().split()))
num = int(input())
for i in range(num):
    operation = input().split()
    if operation[0] == 'intersection_update':
        set_A &= set(map(int, input().split()))
    elif operation[0] == 'update':
        set_A |= set(map(int, input().split()))
    elif operation[0] == 'difference_update':
        set_A -= set(map(int, input().split()))
    elif operation[0] == 'symmetric_difference_update':
        set_A ^= set(map(int, input().split()))
print(sum(set_A))

"""
Task
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b .

Input Format
The first line contains the first integer, , and the second line contains the second integer, .

Output Format
Print the result as described above.

"""
a = int(input())
b = int(input())
for num in divmod(a, b):
    print(num)
print(divmod(a, b))

"""
Input Format

One line of input: an integer N.

Constraints

0 <= N <= 15

Output Format

A list on a single line containing the cubes of the first N fibonacci numbers.

"""

cube = lambda x: x**3
def fibonacci(n):
    if n == 0:
        res = []
    elif n == 1:
        res = [0]
    elif n == 2:
        res = [0, 1]
    else:
        i = 2
        res = [0, 1]
        while i < n:
            res.append(res[-1] + res[-2])
            i+=1
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

"""
Input Format

First line contains n, the number of rational numbers.
The ith of next n lines contain two integers each, the numerator( Ni ) and denominator( Di ) of the  rational number in the list.

Constraints
1 <= n <= 100
1 <= Ni, Di <= 10**9
Output Format

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.

"""
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs, 1)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)