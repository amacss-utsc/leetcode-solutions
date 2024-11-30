# https://leetcode.com/problems/two-sum/

class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution 1 - check each pair of elements using nested loops
        # Time Complexity: O(n^2) because of nested loops 
        n = len(nums)

        for i in range(n):
            curr = nums[i] 
                
            # Checking all elements we have not yet paired with curr 
            for j in range(i + 1, n): 

                 # Ensuring we do not return the same element twice
                if j != i and curr + nums[j] == target:
                    return [i,j]
        return [] 
    

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution 2 - check each pair of elements using a dictionary (2 passes)
        # Pass through nums twice separately, once to populate nums_dict and once more to find the pair 
        # Time Complexity: O(n), since 2n is still linear
        n = len(nums)
        nums_map = {}

        # Creating the map for each index in nums
        for i in range(n):
           nums_map[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
        
            # Ensuring we do not return the same element twice
            if complement in nums_map and nums_map[complement] != i:
                return [i, nums_map[complement]]

        return [] 

class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution 3 - check each pair of elements using a dictrionary (1 pass)
        # Pass through nums once, add each element to nums_map if its complement is not already in nums_map
        # Time Complexity: O(n)
        n = len(nums)
        nums_map = {}
        
        for i in range(n):
            complement = target - nums[i]
        
             # If the current element'a complement is already in nums_map we return the pair 
            if complement in nums_map:
                return [nums_map[complement], i]
            
            # Add the current element to nums_map
            nums_map[nums[i]] = i

        return [] 