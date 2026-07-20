
#include <vector>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;

struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {

private:
    void dfs(TreeNode* node, int row, int col, vector<tuple<int, int, int>>& nodes) {
        if (node == nullptr) {
            return;
        }

        nodes.push_back({col, row, node->val});

        dfs(node->left, row + 1, col - 1, nodes);
        dfs(node->right, row + 1, col + 1, nodes);
    }
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<tuple<int, int, int>> nodes;
        map<int, vector<int>> res;

        dfs(root, 0, 0, nodes);

        sort(nodes.begin(),nodes.end());

        for(auto& [col,row,value] : nodes){
            res[col].push_back(value);
        }

        vector<vector<int>> ans;

        for(auto& [col,values] : res){
            ans.push_back(values);
        }
        return ans;

        
    }
};