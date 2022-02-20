class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(reverse=True,key=lambda x: (x[1],-x[0]))
        count=len(intervals)
        for i in range(len(intervals)-1):
            if intervals[i+1][0]>=intervals[i][0] and intervals[i+1][1]<=intervals[i][1]:
                count-=1
                intervals[i+1]=intervals[i]
        return count