# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head

        curr=head
        while curr and curr.next:
            A=curr
            B=curr.next
            next_pair=B.next

            #swapping
            B.next=A
            A.next=next_pair
            prev.next=B

            prev=A
            curr=next_pair
            
        return dummy.next



        
        