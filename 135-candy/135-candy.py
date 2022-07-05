class Solution:
    def candy(self, ratings: List[int]) -> int:
        res=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]: # left to right iteration 
                res[i]=res[i-1]+1
        for i in range(len(ratings)-1,0,-1): # right to right iteration 
            if ratings[i-1]>ratings[i]:
                res[i-1]=max(res[i-1],res[i]+1)
        return sum(res)