class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        dp=[0]*n
        dp[0],dp[1]=nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[n-1]
        
        
        
        # if len(nums)<=2:
        #     return max(nums)
        # a,b=nums[0],max(nums[0],nums[1])
        # for i in range(2,len(nums)):
        #     temp=a
        #     a=b
        #     b=max(nums[i]+temp,b)
        # return b