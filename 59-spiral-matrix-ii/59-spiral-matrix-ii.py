class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        if n == 1:
            return [[1]]
        res=[[0]*n for _ in range(n)]
        k=1
        direction="forward"
        rowb,rowe=0,n-1
        colb,cole=0,n-1
        while rowb<=rowe and colb<=cole:
            if direction=="forward":
                for i in range(colb,cole+1):
                    res[rowb][i]=k
                    k+=1
                rowb+=1
                direction="downward"
            elif direction=="downward":
                for i in range(rowb,rowe+1):
                    res[i][cole]=k
                    k+=1
                cole-=1
                direction="backward"
            elif direction=="backward":
                for i in range(cole,colb-1,-1):
                    res[rowe][i]=k
                    k+=1
                rowe-=1
                direction="upward"
            else:
                for i in range(rowe,rowb-1,-1):
                    res[i][colb]=k
                    k+=1
                colb+=1
                direction="forward"
        return res
        
        
        