# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        ans=0
        high=n
        while low<=high:
            mid=(low+high)//2
            if isBadVersion(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        