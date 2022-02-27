class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=currmax=currmin=nums[0]
        for i in range(1,len(nums)):
            compare=(currmax*nums[i],currmin*nums[i],nums[i])
            currmax,currmin=max(compare),min(compare)
            res=max(res,currmax)
        return res