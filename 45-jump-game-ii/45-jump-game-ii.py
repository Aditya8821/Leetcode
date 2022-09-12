class Solution:
    def jump(self, nums: List[int]) -> int:
        steps=0
        farthest=0
        farend=0
        for i in range(len(nums)-1):
            farthest=max(farthest,nums[i]+i)
            if i==farend:
                steps+=1
                farend=farthest
        return steps
        
        
        
        # steps=0
        # left,right=0,0
        # while right<len(nums)-1:
        #     farthest=0
        #     for i in range(left,right+1):
        #         farthest=max(farthest,nums[i]+i)
        #     left=right+1
        #     right=farthest
        #     steps+=1
        # return steps
        
      
        
    
        
        
        
        
        
        
        