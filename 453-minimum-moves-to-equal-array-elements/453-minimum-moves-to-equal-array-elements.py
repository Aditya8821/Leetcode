class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minele=min(nums)
        n=0
        for num in nums:
            n+=num-minele
        return n