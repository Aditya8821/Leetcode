class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastposition=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=lastposition:
                lastposition=i
        return lastposition==0
  