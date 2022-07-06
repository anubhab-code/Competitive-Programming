#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        dic = defaultdict(dict)
        
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        ans = sorted(dic, key=dic.get, reverse=True)
        return ans[:k]
        
# @lc code=end

