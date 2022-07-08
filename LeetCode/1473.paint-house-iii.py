#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#

# @lc code=start
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def min_cost_helper(i, prev_color, groups):
            if i == m:
                return 0 if groups == target else float('inf')
            
            if houses[i] != 0:
                return min_cost_helper(i + 1, houses[i], groups + int(prev_color != houses[i]))
            
            total = float('inf')
            for color in range(1, n + 1):
                total = min(total, cost[i][color - 1] + min_cost_helper(i + 1, color, groups + int(prev_color != color)))
            
            return total
        
        ans = min_cost_helper(0, -1, 0)
        return ans if ans != float('inf') else -1   
# @lc code=end

