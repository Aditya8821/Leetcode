class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        start=0
        end=0
        n=len(string)
        longest=0
        d={}
        while end<=n-1:
            d[string[end]]=d.get(string[end],0)+1
            if len(d)==end-start+1:
                longest=max(longest,end-start+1)
                end+=1
            else:
                if d[string[start]]==1:
                    del d[string[start]]
                    start+=1
                    end+=1
                else:
                    d[string[start]]-=1
                    start+=1
                    end+=1
        return longest
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''n = len(string)
        s = 0 
        e = 0
        d = {} 
        ans = 0
        while e<=n-1:
            d[string[e]] = d.get(string[e],0)+1  #This d will store the frequency of chars in the window only
            if len(d)==e-s+1:
                ans = max(ans,e-s+1) #This ans will store the max size of window or substring possible
                e+=1 
            else:
                if d[string[s]]==1: #If the frequency of the start char is only 1 in the current window so delete it from dictionary and move the start pointer forward
                    del d[string[s]]
                    s+=1
                    e+=1 
                else: #If the start char is there in the window there in the current window then decrease it's frqeuency by 1 and move the start pointer forward 
                    d[string[s]]-=1 
                    s+=1
                    e+=1
        return ans
  '''
                
                
            
        
        
        