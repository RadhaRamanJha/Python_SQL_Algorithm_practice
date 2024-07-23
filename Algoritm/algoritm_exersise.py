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
        while w[left] in special_char_set:
            left += 1
        while w[right] in special_char_set:
            right -= 1
        if w[left].lower() != w[right].lower():
            return False
        left += 1
        right -=1
    return True
print(is_palindrome3("A man, a plan, a canal. Panama!"))

## Given a string S, the task is to determine is there exists anoither string that is an anagram of S
## An anagram is a word or phrase formaed by rearranging the letters of another word or phrase

class Solution:
    def doesExists(self, S : str) -> str:
        if S[::-1] != S:
            return 'YES'
        else:
            return 'NO'
        
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        S = (input())

        obj = Solution()
        res = obj.doesExists(S)

        print(res)

# } Driver Code Ends

## Given an array a of size 'n', for each element ai in the array, determine there exists another element in array that is 
## precisisly one less than or one greater than ai, return a binary string of size n, where ith character is 1 if such element 
## exists for ai else 0


class Solution:
    def consecutiveVal(self, n : int, a : List[int]) -> str:
        return_str = ""
        check_set = set(a)
        for i in range(len(a)):
            if (a[i]+1 in check_set) or (a[i]-1 in check_set):
                return_str += '1'
            else:
                return_str += '0'
        return return_str

 