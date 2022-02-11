class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr=[0 for _ in range(26)]
        s2_arr=[0 for _ in range(26)]
        s1_len=len(s1)
        s2_len=len(s2)
        if s1_len>s2_len:
            return False
        start,end=0,0
        while end<s1_len:
            s1_arr[ord(s1[end])-97]+=1
            s2_arr[ord(s2[end])-97]+=1
            end+=1
        end-=1
        while end<s2_len:
            if s1_arr==s2_arr:
                return True
            end+=1
            if end<s2_len:
                s2_arr[ord(s2[end])-97]+=1
            else:
                return False
            s2_arr[ord(s2[start])-97]-=1
            start+=1
        return False
            
            
            
            
           
       