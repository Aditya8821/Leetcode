class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Optimal Solution
        l,r=0,len(height)-1
        res=0
        area=0
        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
        
        
        #Brute Force
        # res=0   
        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         area=(r-l)*min(height[l],height[r])
        #         res=max(area,res)
        # return res