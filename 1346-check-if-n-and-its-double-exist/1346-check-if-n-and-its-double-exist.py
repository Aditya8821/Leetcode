class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i==0 and i in d:
                return True
            else:
                d[i]=0
        if 0 in d: del d[0]
        for i in d:
            if 2*i in d: return True
        return False
            