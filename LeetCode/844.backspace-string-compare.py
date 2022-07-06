#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    backSpace = '#'
    def getIndexAfterBackSpace(self, str, index):
        backSpaceCount = 0
        while(index >= 0):
            if(str[index] == self.backSpace):
                backSpaceCount += 1
            elif(backSpaceCount > 0):
                backSpaceCount -= 1
            else:
                break
            index -= 1
        return index
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s) - 1, len(t) - 1
        
        while(p1 >= 0 and p2 >= 0):
            p1 = self.getIndexAfterBackSpace(s, p1)
            p2 = self.getIndexAfterBackSpace(t, p2)
            if(p1 < 0 or p2 < 0):   break
            if(s[p1] != t[p2]): return False
            p1 -= 1
            p2 -= 1
        p1 = self.getIndexAfterBackSpace(s, p1)
        p2 = self.getIndexAfterBackSpace(t, p2)
        
        if(p1 != p2):   return False
        return True
        
# @lc code=end

