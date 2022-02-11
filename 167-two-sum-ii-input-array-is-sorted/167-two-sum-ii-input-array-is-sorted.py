class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        d={}
        for i in range(len(numbers)):
            if (target-numbers[i]) in d:
                result.append(i+1)
                result.append(d.get(target-numbers[i]))
                return sorted(result)
            d[numbers[i]]=i+1
        return result
            
        