/**
 * Definition for a binary tree node.
 */
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
public:
    int diameter=0;
    int maxH(TreeNode* node){
        if(!node) return 0;

        int L_H=maxH(node->left);
        int R_H=maxH(node->right);

        diameter=max(diameter,L_H+R_H);

        return max(L_H,R_H)+1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        maxH(root);
        return diameter;
    }
};