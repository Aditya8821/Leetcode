class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars or len(chars)==1:
            return len(chars)
        s=""
        s+=chars[0]
        count=1
        for i in range(1,len(chars)):
            if chars[i-1]==chars[i]:
                count+=1
            else:
                if count>1:
                    s+=str(count)
                s+=chars[i]
                count=1
        if count>1:
            s+=str(count)
        for i in range(len(s)):
            chars[i]=s[i]
        chars=chars[:len(s)]
        return len(chars)
        
     