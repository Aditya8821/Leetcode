class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res,pre=0,0
        for row in bank:
            devices=row.count('1')
            if devices==0: 
                continue
            res+=devices*pre
            pre=devices
        return res