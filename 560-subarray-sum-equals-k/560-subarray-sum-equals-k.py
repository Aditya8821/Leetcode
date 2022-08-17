class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_to_index = collections.defaultdict(lambda: [])
        sum_ = 0
        ret = 0
            
            
        for index, number in enumerate(nums):
            sum_ += number
            sums_to_index[sum_].append(index)
            required_sum = sum_ - k
            
            
            if (required_sum in sums_to_index):
                indices = sums_to_index[required_sum]
                last_index = bisect.bisect_left(indices, index)
                ret += last_index
            
            
            if (required_sum == 0):
                ret += 1
                
        return ret
        
             