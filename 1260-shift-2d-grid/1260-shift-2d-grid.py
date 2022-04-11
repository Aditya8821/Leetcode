class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            for i in range(len(grid)):
                if i>0:
                    grid[i].insert(0,temp)
                temp=grid[i].pop()
            grid[0].insert(0,temp)
        return grid