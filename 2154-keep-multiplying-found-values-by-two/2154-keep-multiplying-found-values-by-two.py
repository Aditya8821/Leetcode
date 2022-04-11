class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        flag=0
        while flag==0:
            if original in nums:
                original*=2
            else:
                flag=1
        return original
                