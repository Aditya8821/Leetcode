class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1=list(num1)
        s2=list(num2)
        print(s1)
        print(s2)
        carry=0
        res=[]
        while s1 or s2 or carry:
            if s1:
                carry+=(ord(s1.pop())-48)
            if s2:
                carry+=(ord(s2.pop())-48)
            val=carry%10
            carry=carry//10
            res.insert(0,str(val))
        print(res)
        res="".join(res)
        return res
                