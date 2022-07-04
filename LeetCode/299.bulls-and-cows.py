#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        z=zip(secret,guess)
        bulls=0
        cows=0
        for x,y in z:
            if x==y:
                bulls+=1    
        s=Counter(secret)
        g=Counter(guess)
        for x in g.keys():
            if x in s:
                cows+=min(g[x],s[x])
        cows-=bulls
        return str(bulls)+'A'+str(cows)+'B'
        
# @lc code=end

