class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d=[set(i) for i in words]
        maxval=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (d[i]&d[j]):
                    maxval=max(maxval,len(words[i])*len(words[j]))
        return maxval
        
        
        
        
        
        
        
        
        
        
        
        
        
        