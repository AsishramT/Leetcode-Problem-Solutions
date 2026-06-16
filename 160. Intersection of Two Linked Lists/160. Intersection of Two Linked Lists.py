# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=0
        lenB=0
        curr1=headA
        curr2=headB

        while curr1:
            lenA+=1
            curr1=curr1.next
        
        while curr2:
            lenB+=1
            curr2=curr2.next
            

        lengthDiff=abs(lenA-lenB)

        if lenA>lenB:
            for _ in range(lengthDiff):
                if headA and headA.next:
                    headA=headA.next
        else:
            for _ in range(lengthDiff):
                if headB and headB.next:
                    headB=headB.next
        
        while headA and headB:
            if headA==headB:
                return headA
            
            headA=headA.next
            headB=headB.next


        

        return None

#solution 2 shorter code(switching method)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A=headA
        B=headB

        while A!=B:
            if A:
                A=A.next
            else:
                A=headB
            if B:
                B=B.next
            else:
                B=headA
        return A
