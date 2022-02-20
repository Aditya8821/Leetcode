class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ele=board[i][j]
                if ele!='.':
                    k=(i//3)*3-j//3
                    if ele not in rows[i]:
                        rows[i].add(ele)
                    else:
                        return False
                    if ele not in cols[j]:
                        cols[j].add(ele)
                    else:
                        return False
                    if ele not in boxes[k]:
                        boxes[k].add(ele)
                    else:
                        return False
        return True
                        