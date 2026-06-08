# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        curr=head
        array=[]

        prev=dummy

        while curr:
            array.append(curr.val)
            curr=curr.next
        
        array[k-1], array[-k]= array[-k], array[k-1]
        for val in array:
            prev.next=ListNode(val)
            prev=prev.next
        
        return dummy.next
        

        