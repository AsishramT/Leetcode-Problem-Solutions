class Solution {
public:

    struct pair_hash {
        size_t operator()(const pair<int,int>& p) const {
            return hash<int>()(p.first) ^ hash<int>()(p.second);
        }
    };

    unordered_set<pair<int,int>,pair_hash> safe = {};
    vector<pair<int,int>> direction = {{0,1},{0,-1},{-1,0},{1,0}};

    void dfs(vector<vector<char>>& board,int r, int c){
        if (board[r][c] != 'O' || safe.contains({r,c})) {
            return;
        }

        safe.insert({r,c});

        for(auto dir : direction){
            int nr = r + dir.first;
            int nc = c + dir.second;

            if (nr < 0 || nr >= board.size() ||
                nc < 0 || nc >= board[0].size()) {
                continue;
            }
            if(board[nr][nc]=='O'){
                dfs(board,nr,nc);
            }

        }

    }
    void solve(vector<vector<char>>& board) {
        

        //l and r side
        for(int r=0; r< board.size(); r++){
            dfs(board,r,0);
            dfs(board,r,board[0].size()-1);
        }
        
        //top bot side
        for(int c=0; c< board[0].size(); c++){
            dfs(board,0,c);
            dfs(board,board.size()-1,c);
        }

        for(int i=0; i<board.size();i++){
            for(int j=0; j<board[0].size();j++){
                if (safe.contains({i,j})){
                    continue;
                }
                else{
                    board[i][j]='X';
                }
            }
        }

        
    }
};