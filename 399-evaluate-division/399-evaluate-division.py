class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i, equation in enumerate(equations):
            x,y = equation
            graph[x].append((y,values[i]))
            graph[y].append((x, 1/values[i]))
        def dfs(curr, end, ans):
            if curr in visited: return False
            if(curr == end and end in graph):
                results.append(ans)
                return True
            visited.add(curr)
            for x, y in graph[curr]:
                if(dfs(x, end, ans * y)): return True
            visited.remove(curr)
            return False
            
        results = []
        for q in queries:
            visited = set()
            if(not dfs(q[0], q[1], 1)): results.append(-1)  
        return results