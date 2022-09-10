class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def helper(stack,open,close):
            if len(stack)==2*n:
                res.append("".join(stack))
                return 
            if open<n:
                stack.append("(")
                helper(stack,open+1,close)
                stack.pop()
            if close<open:
                stack.append(")")
                helper(stack,open,close+1)
                stack.pop()
        helper(stack,0,0)
        return res