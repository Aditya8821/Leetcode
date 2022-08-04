class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n==1:
            return nums[0]
        else:
            if nums[0]!=nums[1]:
                return nums[0]
            elif nums[n-1]!=nums[n-2]:
                return nums[n-1]
        for i in range(1,n,3):
            if nums[i]!=nums[i-1] and nums[i]==nums[i+1]:
                return nums[i-1]
        
         