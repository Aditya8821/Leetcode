class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2==0:
            mid=(len(nums)//2)-1
        else:
            mid=len(nums)//2
        s=0
        midele=nums[mid]
        for num in nums:
            if num<midele: 
                s+=midele-num
            else:
                s+=num-midele
        return s
        
        
        
        
        # minele=min(nums)
        # maxele=max(nums)
        # i,j=0,0
        # for num in nums:
        #     i+=num-minele
        #     j+=maxele-num
        # return min(i,j)