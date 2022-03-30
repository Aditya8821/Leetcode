class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        total_sum=sum(card)
        n=len(card)
        l=0
        r=n-k-1
        window_sum=sum(card[0:r+1])
        s=total_sum-window_sum
        l+=1
        r+=1
        print(s)
        while r<len(card):
            window_sum=window_sum-card[l-1]+card[r]
            s=max(s,total_sum-window_sum)
            print(s)
            l+=1
            r+=1
        return s
            
        