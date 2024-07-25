# 1. Maximum sum subarray of size ' k '
def MaxSumSubarray(arr, k):
    start, current_sum, max_sum = 0, 0, 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, current_sum)
            current_sum = current_sum - arr[i-k+1]
    return max_sum
# print(MaxSumSubarray([4,5,6,7,12,2,3,18,1,3],4))

# 2. Count Occurrences of Anagram
def isAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        char_dict = dict()
        for chr in s1:
            if chr in char_dict:
                char_dict[chr] += 1
            else:
                char_dict[chr] = 1
        for chr in s2:
            if chr in char_dict:
                char_dict[chr] -= 1
            else:
                return False
        fv_list = list(char_dict.values())
        for value in fv_list:
            if value != 0:
                return False
        return True
# print(isAnagram("hello","lehlo"))
# print(isAnagram("olep","lehlo"))

def count_anagram(text, word):
    cstring, anagram_count = "", 0
    for i in range(len(text)):
        cstring += text[i]
        if len(cstring) == len(word):
            if isAnagram(cstring, word):
                anagram_count += 1
            cstring = cstring[1:]
    return anagram_count
print(count_anagram('gotxxotgxdogt', 'got'))
print(count_anagram('otgotxxotgxdogto', 'got'))