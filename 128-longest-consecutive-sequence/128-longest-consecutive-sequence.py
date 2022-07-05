class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        maxlen=0
        num=set(nums)
        for item in num:
            if item-1 not in num:
                count=1
                next_item=item+1
                while next_item in num:
                    count+=1
                    next_item+=1
                maxlen=max(maxlen,count)
        return maxlen