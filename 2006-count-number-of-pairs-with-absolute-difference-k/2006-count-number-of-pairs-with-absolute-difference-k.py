class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res=0
        seen=defaultdict(int)
        for i in nums:
            res+= seen[i-k] + seen[i+k]
            seen[i]+=1
        return res
        
       