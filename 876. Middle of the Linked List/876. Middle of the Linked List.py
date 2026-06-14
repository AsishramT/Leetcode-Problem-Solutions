# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1
        
        mid = length // 2
        
        i=0
        while head and i<mid:
            head=head.next
            i+=1
        return head


        