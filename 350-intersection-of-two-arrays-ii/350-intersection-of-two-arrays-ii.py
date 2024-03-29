class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        res=[]
        for i in nums1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in nums2:
            if i in d:
                if d[i]==1:
                    del d[i]
                else:
                    d[i]-=1
                res.append(i)
        return res
        
        # counter1, counter2 = Counter(nums1), Counter(nums2)
        # counter = counter1 & counter2
        # return list(counter.elements())
    
    
        # res=[]
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        #         nums2.remove(i)
        # return res