class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers=[2**i for i in range(22)]
        d={}
        count=0
        for i in deliciousness:
            for j in powers:
                if j-i in d:
                    count+=d[j-i]
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return count%(10**9 + 7)