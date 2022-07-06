#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums):
        ans = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                currnum = num
                currmax = 1
                while currnum+1 in num_set:
                    currnum += 1
                    currmax += 1

                ans = max(ans, currmax)

        return ans
        
# @lc code=end

