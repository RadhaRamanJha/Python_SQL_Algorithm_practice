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