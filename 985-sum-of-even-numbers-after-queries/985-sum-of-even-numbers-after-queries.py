class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=sum(x for x in nums if x%2==0)
        res=[]
        for val,ind in queries:
            if nums[ind]%2==0: s-=nums[ind]
            nums[ind]+=val
            if nums[ind]%2==0: s+=nums[ind]
            res.append(s)
        return res
            