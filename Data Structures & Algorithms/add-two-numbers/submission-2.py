# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        returnList = ListNode()
        returnPtr = returnList

        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 != None else 0
            l2Val = l2.val if l2 != None else 0
            sum = l1Val + l2Val + carry
            nextNode = ListNode(sum % 10)
            carry = sum // 10
            returnList.next = nextNode
            returnList = returnList.next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        return returnPtr.next
