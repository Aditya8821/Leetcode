class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start,end=0,len(nums)-1
        if len(nums)==1:
            return 0
        while start<end:
            mid=(end+start)//2
            if nums[mid]>nums[mid+1]:
                end=mid
            else:
                start=mid+1
        return start
        
        
        # left = 0
        # right = len(nums)-1
        # if len(nums)==1:
        #     return 0
        # while left<=right:
        #     mid=(left+right)//2
        #     if mid==0:    # When first element is the peak 
        #         if nums[mid]>nums[mid+1]:
        #             return mid
        #         else:
        #             left=mid+1
        #     elif mid==len(nums)-1:   # When last element is the peak 
        #         if nums[mid]>nums[mid-1]:
        #             return mid
        #         else:
        #             right=mid-1
        #     elif nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]: #When mid element is peak
        #         return mid
        #     elif nums[mid]>nums[mid+1] and nums[mid]<nums[mid-1]: 
        #         right = mid-1
        #     else:
        #         left = mid+1
            