class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def solve(candidates,tar,res,idx):
            if tar==0:
                ans.append(res[:])
                return
            if tar<0:
                return
            for index in range(idx,len(candidates)):
                res.append(candidates[index])
                solve(candidates,tar-candidates[index],res,index)
                res.pop()
        solve(candidates,target,[],0)
        return ans