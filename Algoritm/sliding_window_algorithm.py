# Maximum sum subarray of size ' k '
def MaxSumSubarray(arr, k):
    start, current_sum, max_sum = 0, 0, 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, current_sum)
            current_sum = current_sum - arr[i-k+1]
    return max_sum
print(MaxSumSubarray([4,5,6,7,12,2,3,18,1,3],4))