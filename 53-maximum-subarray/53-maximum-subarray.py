class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        for index,num in enumerate(nums):
            dp[index]=max(dp[index-1]+num,num)
        return max(dp)
        
        
        '''sum,maxsum=nums[0],nums[0]
        for i in range(1,len(nums)):
            sum=max(sum+nums[i],nums[i])
            maxsum=max(maxsum,sum)
        return maxsum
        '''