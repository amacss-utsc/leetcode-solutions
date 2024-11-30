from typing import List

'''
intuition:

our priority is to find out which words are actually anagrams of each other
to do this, we can consider splitting each word into a list of its chars
ex: ate -> ['a', 't', 'e']

then, sort this list, so that anagrams would result in outputting the same list of chars
ex: ate: ['a', 't', 'e'] -> sorted: ['a', 'e', 't'],
eat: ['e', 'a', 't'] -> sorted: ['a', 'e', 't']
notice that the sorted char list of ate and eat match, as they are anagrams.


now, the best approach to finding all anagrams is to create a frequency dictionary, 
since we can't have lists as keys, our key can be the concatenated string of our
list of sorted chars. ex: ['a', 'e', 't'] -> "aet"
and the value being the original word
ex: {aet: ['eat', 'tea', 'ate']}

finally, return all the values in the dict as a list

https://leetcode.com/problems/group-anagrams/description/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for i in range(len(strs)):

            # create our sorted list of chars (sorted(list) returns the sorted list)
            sorted_chars = sorted(strs[i])

            # create our concantenated string (ex. aet)
            sorted_string = ''.join(sorted_chars) 

            # new anagram found, create a new key-value pair
            if sorted_string not in freq:
                freq[sorted_string] = [strs[i]]
            
            # anagram of existing pair found, append it to list of respective anagrams
            else:
                freq[sorted_string].append(strs[i])
            
        return list(freq.values())

                


        





        