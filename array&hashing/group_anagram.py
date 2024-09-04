# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# Hash Usage - HashMap
# Time - O(m*n)
# Space - O(n)
# Sort huruf yang setipe(sorted), terus di append berdasarkan group(sorted) yang sama

class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            res[key].append(word)
        
        return res.values()
        