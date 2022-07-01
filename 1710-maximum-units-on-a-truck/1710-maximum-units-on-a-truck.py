class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        max_unit=0
        for box in boxTypes:
            if truckSize<0:
                break
            max_unit+=min(truckSize,box[0])*box[1]
            truckSize-=box[0]
        return max_unit
        
        
        
        
        
        # boxTypes=sorted(boxTypes, key = lambda x: -x[1])
        # t=0
        # s=0
        # for i in boxTypes:
        #     if truckSize==0:
        #         return s
        #     for j in range(i[0]):
        #         if truckSize==0:
        #             return s
        #         s+=i[1]
        #         truckSize-=1
        # return s