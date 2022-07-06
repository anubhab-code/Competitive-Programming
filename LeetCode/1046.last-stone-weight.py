#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            a = stones.pop(stones.index(max(stones)))
            b = stones.pop(stones.index(max(stones)))
            if a > b:
                stones.append(a - b)
        return stones[0] if stones else 0
        
# @lc code=end

