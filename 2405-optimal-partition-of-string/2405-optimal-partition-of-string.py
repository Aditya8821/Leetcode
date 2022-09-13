class Solution:
    def partitionString(self, s: str) -> int:
        count=0
        left=0
        right=1
        while right<len(s):
            count+=1
            h=set()
            h.add(s[left])
            while right<len(s):
                if s[right] not in h:
                    h.add(s[right])
                    right+=1
                else:
                    left=right
                    right+=1
                    break
        if left==len(s)-1:
            count+=1
        return count