class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_arr,p_arr=[0]*26,[0]*26
        start,end=0,0
        slen=len(s)
        plen=len(p)
        res=[]
        if slen<plen:
            return res
        while end<plen:
            s_arr[ord(s[end])-97]+=1
            p_arr[ord(p[end])-97]+=1
            end+=1
        end-=1
        while end<slen:
            if s_arr==p_arr:
                res.append(start)
            end+=1
            if end<slen:
                s_arr[ord(s[end])-97]+=1
            else:
                return res
            s_arr[ord(s[start])-97]-=1
            start+=1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
      