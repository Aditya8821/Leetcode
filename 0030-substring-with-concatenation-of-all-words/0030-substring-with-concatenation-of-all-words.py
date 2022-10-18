class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # total=len(words[0])*len(words)
        # single=len(words[0])
        # x,y=0,total
        # f=[]
        # res=[]
        # while y<len(s):
        #     sample=s[x:y]
        #     a,b=0,single
        #     flag=0
        #     for _ in range(len(words)):
        #         if sample[a:b] in words:
        #             a+=single
        #             b+=single
        #         else:
        #             flag=1
        #             break
        #     if flag==0:
        #         res.append(x)
        #     x+=1
        #     y+=1  
        # return res
        
        wlen = len(words[0])
        wslen = len(words) * len(words[0])
        res = []
        for pos in range(wlen):
            i = pos
            d = Counter(words)
            
            for j in range(i, len(s) + 1 - wlen, wlen):
                word = s[j: j + wlen]
                d[word] -= 1
                
                while d[word] < 0:
                    d[s[i: i + wlen]] += 1
                    i += wlen
                if i + wslen == j + wlen:
                    res. append(i)
        return res
                
        
        