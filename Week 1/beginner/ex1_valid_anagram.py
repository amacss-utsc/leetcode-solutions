# https://leetcode.com/problems/valid-anagram/

from collections import Counter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1 - Sort both strings and compare
        # Time Complexity: O(nlogn) - why? https://www.jmoisio.eu/en/blog/2020/09/12/why-sorting-cannot-be-done-faster-n-log-n/
        # In general, any built in sorting algorithm has a time complexity of O(nlogn)
        # Can we do better? (if need be we can briefly touch on time complexity)
        return sorted(s) == sorted(t)
    
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 2: loop through s and t, counting the number of occurrences of each letter
        # How can we track the number of occurrences of each letter? With a hashmap! (dictionary in python)
        # If s and t have the same number of occurrences of every letter, we can say they're anagrams. Otherwise, they're not
        # O(n) since we only do 1 pass over each string, better than sorting!
        if len(s) != len(t):
            return False
        
        # dictionaries for keeping track of occurrences of each letter in each string
        s_letter_count, t_letter_count = {}, {}

        # We know len(s) == len(t)
        for i in range(len(s)):
            s_letter_count[s[i]] = s_letter_count.get(s[i], 0) + 1
            t_letter_count[t[i]] = t_letter_count.get(t[i], 0) + 1
        
        return s_letter_count == t_letter_count
    
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 3: Same as solution 2, but uses the Counter() function from python's collections library. Know your tools!
        # Sometimes they wouldn't let you use stuff like this in interviews, but otherwise it saves you time

        return Counter(s) == Counter(t)
        