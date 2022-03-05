class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        nums.sort()
        for num in nums:
            res+=[curr+[num] for curr in res if curr+[num] not in res]
        return res
    