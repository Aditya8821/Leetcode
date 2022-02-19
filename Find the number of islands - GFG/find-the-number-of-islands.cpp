// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    // Function to find the number of islands.
    void dfs(int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& vis) {
        if(i<0 or i>=grid.size() or j<0 or j>=grid[0].size()) return;
        if(vis[i][j] or grid[i][j] == '0') return;
        
        vis[i][j] = true;
        dfs(i-1, j, grid, vis);
        dfs(i, j+1, grid, vis);
        dfs(i+1, j, grid, vis);
        dfs(i, j-1, grid, vis);
        dfs(i+1, j+1, grid, vis);
        dfs(i+1, j-1, grid, vis);
        dfs(i-1, j+1, grid, vis);
        dfs(i-1, j-1, grid, vis);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        
        int res = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(grid[i][j] == '1' and !vis[i][j]){
                    dfs(i, j, grid, vis);
                    res++;
                }
            }
        }
        
        return res;
    }
};

// { Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}  // } Driver Code Ends