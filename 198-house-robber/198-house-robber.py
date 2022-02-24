class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        a,b=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=a
            a=b
            b=max(nums[i]+temp,b)
        return b