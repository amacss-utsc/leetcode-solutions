# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


# Most efficient approach: Using Two Pointer technique for O(n) time complexity

# Intuition:

# We use the fact that the array is sorted and there exists two values s.t. their sum is target.

# Depending on if the sum on the current iteration of our while loop is less than or greater than target, we can move our left and right pointer towards the centre (increment or decrement) respectively to find values that sum to target

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        indices = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                indices.append(l + 1)
                indices.append(r + 1)
                break
            elif numbers[l] + numbers[r] < target:
                l += 1

            else:
                r -= 1
        
        return indices
