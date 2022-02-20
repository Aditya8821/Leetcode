class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def solve(sub,i):
            if len(sub)==len(s):
                final.append(sub)
                return 
            else:
                if s[i].isalpha():
                    solve(sub+s[i].swapcase(),i+1)
                solve(sub+s[i],i+1)
        final=[]
        solve("",0)
        return final