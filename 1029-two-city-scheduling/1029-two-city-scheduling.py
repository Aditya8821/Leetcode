class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        mincost=0
        diff=[]
        for A,B in costs:
            diff.append(B-A)
            mincost+=A
        diff.sort()
        for i in range(len(costs)//2):
            mincost+=diff[i]
        return mincost
                
            
                