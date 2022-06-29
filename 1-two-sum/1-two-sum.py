class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        d={}
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                res.append(i)
                res.append(d.get(target-nums[i]))
                return res
            else:
                d[nums[i]]=i
        return result