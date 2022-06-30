class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        midele=nums[len(nums)//2]
        for num in nums:
            s+=abs(midele-num)
        return s
            
        
        
        # nums.sort()
        # if len(nums)%2==0:
        #     mid=(len(nums)//2)-1
        # else:
        #     mid=len(nums)//2
        # s=0
        # midele=nums[mid]
        # for num in nums:
        #     if num<midele: 
        #         s+=midele-num
        #     else:
        #         s+=num-midele
        # return s
        
        
        
        
     