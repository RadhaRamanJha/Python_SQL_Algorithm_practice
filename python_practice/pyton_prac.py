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