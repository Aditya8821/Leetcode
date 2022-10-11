class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res=[]
        i=0
        d={}
        while (i+9)<len(s):
            if s[i:i+10] not in d:
                d[s[i:i+10]]=1
            elif s[i:i+10] not in res:
                res.append(s[i:i+10])
            i+=1
        return res