# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list=[]
        for LL in lists:
            curr=LL
            while curr:
                new_list.append(curr.val)
                curr=curr.next
        new_list.sort()

        dummy=ListNode(0)
        curr=dummy
        

        for val in new_list:
            curr.next=ListNode(val)
            curr=curr.next
        return dummy.next

        