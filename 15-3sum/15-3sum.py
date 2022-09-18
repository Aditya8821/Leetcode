class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            target=-nums[i]
            while l<r:
                if nums[l]+nums[r]==target:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        return list(res)
        
        
        
        # nums=sorted(nums)
        # res=set()
        # for i in range(len(nums)):
        #     l=i+1
        #     r=len(nums)-1
        #     target=-nums[i]
        #     while l<r:
        #         if nums[l]+nums[r]==target:
        #             res.add((nums[i],nums[l],nums[r]))
        #             l+=1
        #             r-=1
        #         elif nums[l]+nums[r]<target:
        #             l+=1
        #         else:
        #             r-=1
        # return list(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     