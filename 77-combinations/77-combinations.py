class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final=[]
        def solve(remain,val,comb,final):
            if remain==0:
                final.append(comb.copy())
            else:
                for i in range(val,n+1):
                    comb.append(i)
                    solve(remain-1,i+1,comb,final)
                    comb.pop()
        solve(k,1,[],final)
        return final
        
        
        
        
        
        # res=[[]]
        # for num in range(1,n+1):
        #     res+=[curr+[num] for curr in res]
        # # print(res)
        # ans=[]
        # for i in res:
        #     if len(i)==k:
        #         ans.append(i)
        # return ans
  