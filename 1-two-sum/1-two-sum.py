class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                res.append(i)
                res.append(d.get(target-nums[i]))
                return res
            d[nums[i]]=i