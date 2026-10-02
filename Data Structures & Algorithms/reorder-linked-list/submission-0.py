# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the midpoint of the list 
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # slow is now the midpoint
        # reverse the second half of the list
        second = slow.next
        slow.next = None
        prev = None

        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two lists
        currNode = head
        reverseNode = prev
        while reverseNode != None:
            temp1 = currNode.next
            temp2 = reverseNode.next
            currNode.next = reverseNode
            reverseNode.next = temp1
            currNode = temp1
            reverseNode = temp2