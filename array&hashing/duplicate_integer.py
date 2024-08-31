# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Hash Usage - Hashset
# Time - O(n) karena make hash set, jadi dia nyimpen di satu set terus scan tiap data apakah punya duplicate sama yang udah disimipen di set
# Space - O(n) alhasil spacenya juga jadi O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:

            if n in hashSet:
                return True

            hashSet.add(n) 

        return False