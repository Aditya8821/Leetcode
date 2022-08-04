class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        if size>1:
            if nums[0]!=nums[1]:
                return nums[0]
            if nums[size-1]!=nums[size-2]:
                return nums[size-1]
        else:
            return nums[0]

        for i in range(1, size, 3):
            if nums[i]!=nums[i-1] and nums[i]==nums[i+1]:
                return nums[i-1]
         