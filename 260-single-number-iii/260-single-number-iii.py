class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        res=[]
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            elif nums[i]!=nums[i+1]:
                res.append(nums[i])
                i+=1
        if nums[-1]!=nums[-2]:
            res.append(nums[-1])
        return res
        