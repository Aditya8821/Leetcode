class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            sum=max(sum+nums[i],nums[i])
            maxsum=max(maxsum,sum)
        return maxsum