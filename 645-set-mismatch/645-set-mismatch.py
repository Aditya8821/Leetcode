class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # x=1
        # ans=[]
        # for i in range(len(nums)):
        #     if nums[i]!=x:
        #             ans.append(nums[i])
        #             ans.append(nums[i]+1)
        #             return ans
        #     x+=1
            
            
            
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]