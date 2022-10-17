class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d={}
        for i in sentence:
            d[i]=d.get(i,0)+1
        return len(d)==26