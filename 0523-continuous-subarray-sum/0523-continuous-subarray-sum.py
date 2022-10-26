class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder={0:-1}
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            if rem in remainder:
                if i-remainder[rem]>1:
                    return True
            else:
                remainder[rem]=i
        return False