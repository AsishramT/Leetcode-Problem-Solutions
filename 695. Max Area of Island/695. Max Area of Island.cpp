class Solution {
public:
    vector<pair<int,int>> direc = {
            {0, 1},
            {0, -1},
            {-1, 0},
            {1, 0}
        };
        
    int dfs(vector<vector<int>>& grid, int r, int c){
        int area = 1;
        grid[r][c] = 0;

        for(auto dir : direc){
            int nr = r + dir.first;
            int nc = c + dir.second;

            if (nr < 0 || nr >= grid.size() ||
                nc < 0 || nc >= grid[0].size()) {
                continue;
            }

            if (grid[nr][nc] == 1 ){
                area+=dfs(grid, nr, nc);
            }
        }

        return area;


    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;

        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j< grid[0].size(); j++){
                if (grid[i][j]==1) {
                    max_area=max(max_area,dfs(grid,i,j));
                }
            }
        }

        return max_area;
        
    }
};