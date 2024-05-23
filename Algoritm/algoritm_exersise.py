# Palindrome word detector
def is_palindrome1(w):
    return w[::-1] == w

def is_palindrome2(w):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]
    return True
## Most optimal algoritm (Time complexity - O(N), Space Complexity - O(1))
def is_palindrome3(w):
    special_char_set = {' ','.',',','!'}
    left, right = 0, len(w)-1
    while left < right:
        while left < right and w[left] in special_char_set:
            left += 1
        while left < right and w[right] in special_char_set:
            right -= 1
        if w[left].lower() != w[right].lower():
            return False
        left += 1
        right -=1
    return True
print(is_palindrome3("A man, a plan, a canal. Panama!"))