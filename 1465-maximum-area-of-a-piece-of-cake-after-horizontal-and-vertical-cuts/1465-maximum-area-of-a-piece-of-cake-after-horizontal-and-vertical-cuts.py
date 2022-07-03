class Solution:
    def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
        def getMaxGap(nums, max_size):
            maxGap = max(nums[0], max_size - nums[-1])
            for i in range(1, len(nums)):
                maxGap = max(maxGap, nums[i] - nums[i - 1])
            return maxGap
        return getMaxGap(sorted(H), h) * getMaxGap(sorted(V), w) % 1000000007