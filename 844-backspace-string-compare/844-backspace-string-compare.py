class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1,l2=[],[]
        for c in s:
            if c=="#" and l1:
                l1.pop() 
            elif c!="#":
                l1.append(c)
        print(l1)
        for c in t:
            if c=="#" and l2:
                l2.pop()
            elif c!="#":
                l2.append(c)
        print(l2)
        return l1==l2
        
       # "y#fo##f"
       #"y#f#o##f"