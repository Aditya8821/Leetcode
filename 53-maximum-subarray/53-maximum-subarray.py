class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp=[0]*len(nums)
        # for index,num in enumerate(nums):
        #     dp[index]=max(dp[index-1]+num,num)
        # return max(dp)
        sum=0
        res=-(1<<31)
        for hey in nums:
            sum+=hey
            res=max(sum, res)
            if sum<0:
                sum=0
            
        return res
        '''sum,maxsum=nums[0],nums[0]
        for i in range(1,len(nums)):
            sum=max(sum+nums[i],nums[i])
            maxsum=max(maxsum,sum)
        return maxsum
        '''