#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        dist=[[int(1e9)]*m for i in range(n)]
        queue=[]
        queue.append(source)
        dist[source[0]][source[1]]=0
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        
        while queue:
            currentblock=queue.pop(0)
            currx=currentblock[0]
            curry=currentblock[1]
            if currx==destination[0] and curry==destination[1]:
                return dist[currx][curry]
            for i in range(4):
                nextx=currx+dx[i]
                nexty=curry+dy[i]
                if self.validblock(nextx,nexty,n,m) and grid[nextx][nexty]==1 and dist[nextx][nexty]==int(1e9):
                    queue.append([nextx,nexty])
                    dist[nextx][nexty]=dist[currx][curry]+1
        return -1
    
    def validblock(self,nextx,nexty,n,m):
        return nextx >= 0 and nextx < n and nexty >= 0 and nexty < m
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends