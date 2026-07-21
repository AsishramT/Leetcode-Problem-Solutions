# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        summ = 0

        dummy = ListNode()
        tail = dummy

        while curr:
            if curr.val==0:
                if summ != 0:
                    tail.next=ListNode(summ,None)
                    tail=tail.next
                    summ=0
            else:
                summ+=curr.val
            
            curr=curr.next
            
        return dummy.next






#O(1) space and O(n) time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        curr = head.next

        while modify:
            total = 0

            while curr.val != 0:
                total += curr.val
                curr = curr.next

            modify.val = total

            curr = curr.next
            modify.next = curr

            modify = curr

        return head.next