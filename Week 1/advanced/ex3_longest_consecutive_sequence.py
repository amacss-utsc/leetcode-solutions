class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maximumLength = 0

        for num in nums:
            if num - 1 not in nums:
                length = 0
                while num in numSet:
                    length += 1
                    num += 1
                maximumLength = max(maximumLength, length)

        return maximumLength

