class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        n=len(columnTitle)-1
        for i in columnTitle:
            val=ord(i)-65+1
            res+=(26**n)*val
            n-=1
        return res