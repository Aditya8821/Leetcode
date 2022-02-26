class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        freq=[0]*(max(nums)+1)
        for num in nums:
            freq[num]+=num
        dp=[0]*(len(freq))
        dp[1]=freq[1]
        for i in range(2,len(dp)):
            dp[i]=max(dp[i-1],freq[i]+dp[i-2])
        return dp[len(freq)-1]
   

       