class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        def solve(index,tar,final,res):
            if tar==0:
                final.append(res.copy())
                return 
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]: continue
                if candidates[i]>tar: break
                res.append(candidates[i])
                solve(i+1,tar-candidates[i],final,res)
                res.pop()
        candidates.sort()
        solve(0,target,final,[])
        return final