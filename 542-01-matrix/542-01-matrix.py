class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # rows = len(mat)
        # cols = len(mat[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if mat[i][j]!=0:
        #             top = mat[i-1][j] if i>0 else float('inf')
        #             right = mat[i][j-1] if j>0 else float('inf')
        #             mat[i][j] = min(top,right)+1
        # for i in range(rows-1,-1,-1):
        #     for j in range(cols-1,-1,-1):
        #         if mat[i][j] !=0:
        #             left = mat[i][j+1] if j<cols -1 else float('inf')
        #             down = mat[i+1][j] if i<rows-1 else float('inf')
        #             mat[i][j] = min(mat[i][j], min(left,down)+1)           #we don't want to change value if top,left is less than bottom right
        # return mat
        
        
        
        row,col=len(mat),len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j]!=0:
                    top=mat[i-1][j] if i>0 else float('inf')
                    left=mat[i][j-1] if j>0 else float('inf')
                    mat[i][j]=min(top,left)+1
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if mat[i][j]!=0:
                    down=mat[i+1][j] if i<row-1 else float('inf')
                    right=mat[i][j+1] if j<col-1 else float('inf')
                    mat[i][j]=min(mat[i][j],min(down,right)+1)
        return mat