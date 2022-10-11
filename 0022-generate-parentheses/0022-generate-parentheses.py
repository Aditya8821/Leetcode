class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def help(stack,open,close):
            if len(stack)==2*n:
                res.append("".join(stack))
                return 
            if open<n:
                stack.append("(")
                help(stack,open+1,close)
                stack.pop()
            if close<open:
                stack.append(")")
                help(stack,open,close+1)
                stack.pop()
        help(stack,0,0)
        return res
        
        