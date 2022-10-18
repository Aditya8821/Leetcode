class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        res="11"
        for i in range(3,n+1):
            t=""
            res+="$"
            c=1
            for j in range(1,len(res)):
                if res[j]==res[j-1]:
                    c+=1
                else:
                    t+=str(c)
                    t+=res[j-1]
                    c=1
            res=t
        return t
            