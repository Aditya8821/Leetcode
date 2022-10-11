class Solution:
    def longestValidParentheses(self,s):
        stack = [-1]
        ans = 0
        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            else:
                stack.pop()
                if stack:
                    ans = max(ans, idx - stack[-1])
                else:
                    stack.append(idx)
        return ans
    