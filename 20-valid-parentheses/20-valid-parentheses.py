class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i]==")" and stack[-1]=="(":
                stack.pop(-1)
            elif s[i]=="]" and stack[-1]=="[":
                stack.pop(-1)
            elif s[i]=="}" and stack[-1]=="{":
                stack.pop(-1)
            else:
                stack.append(s[i])
        return True if not stack else False
    
    
    
    
    
    
    