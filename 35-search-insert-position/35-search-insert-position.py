class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for index,num in enumerate(nums):
            if target<=num:
                return index
        return len(nums)