class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def helper(nums,temp):
            if len(nums)==0:
                if temp not in final:
                    final.append(temp)
                return 
            for i in range(len(nums)):
                print(temp)
                helper(nums[:i]+nums[i+1:],temp+[nums[i]])
        helper(nums,[])
        return final