# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

# Hash Usage - Hash Map
# Bucket Sort
# Di group berdasarkan frequensi angka yang keluar dari tiap digit

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Cara lebih sederhana pake counter terus pilih yang most common aja

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Menghitung frekuensi setiap elemen
        count = Counter(nums)
        
        # Mendapatkan elemen dengan frekuensi tertinggi
        return [num for num, freq in count.most_common(k)] 
