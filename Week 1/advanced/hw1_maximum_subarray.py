# https://leetcode.com/problems/maximum-subarray/description/

# Simple approach: Iterating over all sub-arrays, which has time complexity of O(n^2) 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
    
        # Outer loop for starting point of subarray
        for i in range(len(nums)):
            currSum = 0
        
            # Inner loop for ending point of subarray
            for j in range(i, len(nums)):
                currSum = currSum + nums[j]
            
                # Update max_sum if currSum is greater than the current max_sum
                max_sum = max(max_sum, currSum)
            
        return max_sum

##############            

# Most efficient approach: using Kadane's Algorithm to achieve time complexity of O(n) 

# Intuition:

# If adding the current element (num) to the running sum improves the sum
    # you extend the current subarray to include this element.

# If the running sum (current_sum) ever drops below 0, it's better to start a new subarray from the next element
    # since a negative sum will only decrease the potential sum of subsequent subarrays.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=float('-inf')
        
        for num in nums:
            current_sum += num

            # Update the maximum sum if the current subarray sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

            # If the current subarray sum becomes negative, reset it to 0
            # This signifies that starting a new subarray will yield a better sum
            if current_sum < 0:
                current_sum=0
        return max_sum
        