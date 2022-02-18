class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res=[]
        for n in num:
            while (res and int(res[-1])>int(n) and k):
                res.pop()
                k-=1
            res.append(str(n))
        
        while(k):
            res.pop()
            k-=1
        
        i=0
        while(i<len(res) and res[i]=="0"):
            i+=1
            
        return "".join(res[i:]) if (len(res[i:])>0) else "0"