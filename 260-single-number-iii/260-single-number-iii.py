class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        counter=0
        res=[]
        for k,v in d.items():
            if v==1:
                res.append(k)
                counter+=1
            if counter==2:
                return res