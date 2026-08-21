/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        vector<int> lst = {};
        while (list1 || list2){
            if(list1){
                lst.push_back(list1->val);
                list1 = list1->next;
            }
            if(list2){
                lst.push_back(list2->val);
                list2 = list2->next;
            }
        }
        sort(lst.begin(),lst.end());

        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        for(auto value:lst){
            curr->next =new ListNode(value);
            curr=curr->next;
        }

        return dummy->next;
    }
};