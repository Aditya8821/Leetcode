class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d=defaultdict(list)
        res=[]
        for i,grp in enumerate(groupSizes):
            d[grp].append(i)
            if len(d[grp])==grp:
                res.append(d[grp])
                del d[grp]
        return res
                