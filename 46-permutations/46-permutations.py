class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def helper(nums,temp,final):
            if len(nums)==0:
                final.append(temp)
                return 
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:],temp+[nums[i]],final)
        helper(nums,[],final)
        return final
            