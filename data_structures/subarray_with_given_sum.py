"""
Given a 1-based indexing array arr[] of non-negative integers and an integer sum. 
You mainly need to return the left and right indexes(1-based indexing) of that subarray. 
In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. 
If no such subarray exists return an array consisting of element -1.

Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
Output: [2, 5]
Explanation: Sum of subarray arr[2…5] is 2 + 4 + 8 + 9 = 23.

"""

def subarray_with_given_sum(arr, target):
    if not arr:
        return [-1]
    
    left = 0
    right = 0
    current_sum = arr[0]
    
    while right < len(arr):
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        else:
            current_sum -= arr[left]
            left += 1
    
    return [-1]

# Test subarray_with_given_sum function
print(subarray_with_given_sum([15, 2, 4, 8, 9, 5, 10, 23], 23)) # [2, 5]
print(subarray_with_given_sum([1, 2, 3, 7, 5], 12)) # [2, 4]