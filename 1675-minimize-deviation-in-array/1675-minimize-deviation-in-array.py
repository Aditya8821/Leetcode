from heapq import *
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxHeap=[]
        heapify(maxHeap)
        min_ele=(1<<31)
        for i in nums:
            if i%2==1:
                i*=2
            min_ele=min(min_ele,i)
            heappush(maxHeap,-1*i)
        diff=(1<<31)
        while (-1*maxHeap[0])%2==0:
            top_ele=-1*maxHeap[0]
            heappop(maxHeap)
            heappush(maxHeap,-1*(top_ele//2))
            diff=min(diff,top_ele-min_ele)
            min_ele=min(min_ele,top_ele//2)
        return min(diff,(-1*(maxHeap[0]))-min_ele)
                