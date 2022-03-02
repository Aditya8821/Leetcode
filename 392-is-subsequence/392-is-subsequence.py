class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        def dp(i,j):
            if i==m: return True
            j=t.find(s[i],j)
            if j!=-1:
                return dp(i+1,j+1)
            return False
        m=len(s)
        return dp(0,0)