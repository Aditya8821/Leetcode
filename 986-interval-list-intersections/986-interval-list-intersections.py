class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result=[]
        a,b=firstList,secondList
        i,j=0,0
        start,end=0,1
        while i<len(a) and j<len(b): 
            if (a[i][start]<=b[j][end] and a[i][start]>=b[j][start]) or (b[j][start]>=a[i][start] and b[j][start]<=a[i][end]):
                x=max(a[i][start],b[j][start])
                y=min(a[i][end],b[j][end])
                result.append([x,y])
            if a[i][end]<b[j][end]:
                  i+=1
            else:
                  j+=1
        return result