class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        currmax=0
        ans=0
        for a,d in properties:
            if d<currmax:
                ans+=1
            else:
                currmax=d
        return ans
        
        
        