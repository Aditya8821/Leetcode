class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #O(1) Space solution
        m=len(matrix)
        n=len(matrix[0])
        isfirstcolzero=False 
        isfirstrowzero=False
        for i in range(m):
            if matrix[i][0]==0:
                isfirstcolzero=True #set true if have any one zero in first col
        for i in range(n):
            if matrix[0][i]==0:
                isfirstrowzero=True #set true if have any one zero in first row
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if isfirstcolzero==True:
            for i in range(m):
                matrix[i][0]=0
        if isfirstrowzero==True:
            for i in range(n):
                matrix[0][i]=0
        
        
        
        
        #O(m+n) space solution
        # if not matrix:
        #     return []
        # m,n=len(matrix),len(matrix[0])
        # zeroes_row=[False]*m
        # zeroes_col=[False]*n
        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col]==0:
        #             zeroes_row[row]=True
        #             zeroes_col[col]=True
        # for row in range(m):
        #     for col in range(n):
        #         if zeroes_row[row] or zeroes_col[col]:
        #             matrix[row][col]=0
        # return matrix
