class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[[]]
        for num in range(1,n+1):
            res+=[curr+[num] for curr in res]
        # print(res)
        ans=[]
        for i in res:
            if len(i)==k:
                ans.append(i)
        return ans
  