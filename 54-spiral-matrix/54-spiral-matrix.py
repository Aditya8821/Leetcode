class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        rowb,rowe,colb,cole=0,len(matrix)-1,0,len(matrix[0])-1
        while rowb<=rowe and colb<=cole:
            for i in range(colb,cole+1):
                res.append(matrix[rowb][i])
            rowb+=1
            for i in range(rowb,rowe+1):
                res.append(matrix[i][cole])
            cole-=1
            if rowb<=rowe:
                for i in range(cole,colb-1,-1):
                    res.append(matrix[rowe][i])
                rowe-=1
            if colb<=cole:
                for i in range(rowe,rowb-1,-1):
                    res.append(matrix[i][colb])
                colb+=1
        return res
      
