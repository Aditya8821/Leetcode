class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def helper(nums,temp):
            if len(nums)==0:
                final.append(temp)
                return 
            for i in range(len(nums)):
                print(temp)
                helper(nums[:i]+nums[i+1:],temp+[nums[i]])
        helper(nums,[])
        return final
            