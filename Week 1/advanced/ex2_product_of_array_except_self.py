# https://leetcode.com/problems/product-of-array-except-self/description/

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # Intuition:
    # We pre-compute the prefix and suffix products for each array element i (default 1 if either doesn't exist)
    # Then loop from 0 to len(nums) multiplying the prefix with suffix for final answer

    # left = prefix, right = suffix
    # Initialize with 1 since it doesn't change product
    left = [1]*len(nums)
    right = [1]*len(nums)

    for i in range(1, len(nums)):
        # left to right skipping index 0
        left[i] = left[i-1]*nums[i-1]

        # right to left skipping index len(nums)
        right[i] = right[i - 1] * nums[len(nums) - i]

    # Compute all values and return list (default value doesn't matter because we are reassigning the values anyways)
    final = [0]*len(nums)
    for i in range(0, len(nums)):
        final[i] = left[i] * right[len(nums)-i-1]
    return final