#include <iostream>
#include <vector>
#include <deque>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }

        vector<int> res;
        deque<TreeNode*> q = {root};

        while (!q.empty()) {
            vector<int> level;
            int n = q.size();

            for (int i = 0; i < n; i++) {
                TreeNode* node = q.front();
                q.pop_front();

                level.push_back(node->val);

                if (node->left != nullptr) {
                    q.push_back(node->left);
                }

                if (node->right != nullptr) {
                    q.push_back(node->right);
                }
            }

            res.push_back(level.back());
        }

        return res;
    }
};

