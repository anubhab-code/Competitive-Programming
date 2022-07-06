#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [(1, [])]
        currK = []
        for i in range(len(s)):
            if s[i].isdigit():
                currK.append(s[i])
            elif s[i] == '[':
                k = int("".join(currK))
                stack.append((k, []))
                currK = []
            elif s[i] == ']':
                k, cstr = stack.pop()
                stack[-1][1].extend(k*cstr)
            else:
                stack[-1][1].append(s[i])

        return "".join(stack[0][1])
        
# @lc code=end

