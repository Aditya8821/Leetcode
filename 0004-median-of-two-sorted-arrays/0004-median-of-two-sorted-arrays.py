class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l=len(nums1)
        if l%2!=0:
            return nums1[int(l/2)]
        else:
            x=nums1[int(l/2)]+nums1[int(l/2)-1]
            return x/2