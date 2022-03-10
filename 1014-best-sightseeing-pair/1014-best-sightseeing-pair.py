class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxval, runval = 0, 1
        
        for i, value in enumerate(values):
            runval -= 1
            maxval = max(maxval, value + runval)
            runval = max(value, runval)
            
        return maxval