class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=1
        last={}
        for ch in s:
            old=dp
            dp*=2
            if ch in last:
                dp-=last[ch]
            last[ch]=old
        return (dp-1)%(10**9+7)
        