

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def detect(self,src,adj,vis):
        vis[src]=1
        q=[]
        q.append((src,-1))
        while q:
            node,parent=q.pop(0)
            for adjnode in adj[node]:
                if not vis[adjnode]:
                    vis[adjnode]=1
                    q.append((adjnode,node))
                elif parent!=adjnode:
                    return True
        return False
                    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[0]*(V+1)
		for i in range(V):
		    if not vis[i]:
		        if self.detect(i,adj,vis):
		            return True
		return False
		

#{ 
 # Driver Code Starts


if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends